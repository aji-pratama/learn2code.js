import json
import re

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import (
    View,
    DetailView,
    ListView
)

from app.intrepreters import exec_js
from app.models import Lesson


class LessonListView(ListView):
    template_name = 'index.html'
    context_object_name = 'lessons'
    queryset = Lesson.objects.active()


class LessonDetailView(DetailView):
    model = Lesson
    queryset = Lesson.objects.active()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        obj = self.get_object()

        if obj.get_prev_lesson():
            context['prev_lesson'] = obj.get_prev_lesson()

        if obj.get_next_lesson() and obj.is_correct is True:
            context['next_lesson'] = obj.get_next_lesson()

        context['initial_code'] = self.request.session.get(
            'initial_code_%s' % obj.slug,
            obj.initial_code
        )

        return context

    def get_template_names(self):
        if self.get_object().output_interface == 2:
            return 'lesson/web.html'
        return 'lesson/console.html'


class ConsoleAnswerView(View):

    def post(self, request, slug):
        form_data = json.loads(request.body)
        output = exec_js(form_data['answer_code'])
        obj = Lesson.objects.get(slug=slug)
        output['correct'] = self.validate_answer(obj, output)

        if output['correct'] or obj.get_next_lesson():
            output['next_lesson'] = obj.get_next_lesson()

        # Store answered code to session
        self.request.session['initial_code_%s' % slug] = form_data['answer_code']

        return JsonResponse(output)

    def validate_answer(self, obj, answer_output):
        expected_codes = obj.expectedanswer_set.values_list('expected_code')
        expected_output = []

        for code in expected_codes:
            output = exec_js(code)
            expected_output.append(output)

        # validate output
        answer_correct = False
        if answer_output in expected_output:
            answer_correct = True
            obj.is_correct = True
            obj.save()

        return answer_correct


class WebAnswerView(View):

    @xframe_options_exempt
    def get(self, request, slug):
        code = request.GET.get('code', '')
        obj = Lesson.objects.get(slug=slug)
        return render(request, 'lesson/iframe_output.html', {'code': code, 'obj': obj})

    def post(self, request, slug):
        form_data = json.loads(request.body)
        answer_code = form_data['answer_code']
        obj = Lesson.objects.get(slug=slug)

        output = {
            'answer_code': answer_code,
            'correct': self.validate_answer(obj, answer_code)
        }

        if output['correct'] or obj.get_next_lesson():
            output['next_lesson'] = obj.get_next_lesson()

        # Store answered code to session
        self.request.session['initial_code_%s' % slug] = answer_code

        return JsonResponse(output)

    def validate_answer(self, obj, answer_code):
        clean_answer_code = re.sub(r"[\n\t\s'\\']*", "", answer_code)
        correct = False

        clean_expected_codes = []
        for expected_code in obj.expectedanswer_set.values_list('expected_code', flat=True):
            expected_code = re.sub(r"[\n\t\s'\\']*", "", expected_code)
            clean_expected_codes.append(expected_code)

        if clean_answer_code in clean_expected_codes:
            correct = True
            obj.is_correct = True
            obj.save()

        return correct
