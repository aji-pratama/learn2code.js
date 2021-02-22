import json

from django.http import JsonResponse
from django.views.generic import (
    View,
    DetailView,
    ListView
)

from app.forms import LessonSubmissionForm
from app.intrepreters import exec_js
from app.models import Lesson


class LessonListView(ListView):
    template_name = 'index.html'
    context_object_name = 'lessons'
    queryset = Lesson.objects.active()


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lesson.html'
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_code'] = LessonSubmissionForm()
        return context


class SubmitAnswerView(View):

    def post(self, request, slug):
        form_data = json.loads(request.body)
        output = exec_js(form_data['answer_code'])
        obj_lesson = Lesson.objects.get(slug=slug)
        output['correct'] = self.validate_answer(obj_lesson, output)
        return JsonResponse(output)

    def validate_answer(self, obj_lesson, answer_output):
        expected_codes = obj_lesson.expectedanswer_set.values_list('expected_code')
        expected_output = []

        for code in expected_codes:
            output = exec_js(code)
            expected_output.append(output)

        # validate output
        answer_correct = False
        if answer_output in expected_output:
            answer_correct = True

        return answer_correct
