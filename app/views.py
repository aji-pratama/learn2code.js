import json

from django.http import JsonResponse
from django.urls import reverse_lazy
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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        obj = self.get_object()
        if obj.get_prev_lesson():
            context['prev_lesson'] = reverse_lazy('learn_detail', args=[obj.get_prev_lesson().slug])

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

        if obj.get_next_lesson() and output['correct']:
            output['next_lesson'] = reverse_lazy('learn_detail', args=[obj.get_next_lesson().slug])

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

        return answer_correct


class WebAnswerView(View):

    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code', '')
        return render(request, 'lesson/iframe_output.html', {'code': code})

    def post(self, request, slug):
        form_data = json.loads(request.body)
        answer_code = form_data['answer_code']
        obj = Lesson.objects.get(slug=slug)

        expected_codes = obj.expectedanswer_set.values_list('expected_code')
        validate_answer_code = (True if answer_code in expected_codes else False)

        output = {
            'answer_code': answer_code,
            'correct': validate_answer_code
        }

        if obj.get_next_lesson() and output['correct']:
            output['next_lesson'] = reverse_lazy('learn_detail', args=[obj.get_next_lesson().slug])

        return JsonResponse(output)
