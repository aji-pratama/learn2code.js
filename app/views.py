import json

from django.http import JsonResponse
from django.views.generic import (
    View,
    DetailView,
    ListView
)

from app.forms import LessonSubmissionForm
from app.intrepreter import sandbox
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
        result_answer_code = sandbox(form_data['answer_code'])
        response_data = {
            'console': result_answer_code['result']
        }
        return JsonResponse(response_data)
