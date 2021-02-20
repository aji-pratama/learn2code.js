import json

from django.http import JsonResponse
from django.views.generic import (
    View,
    DetailView,
    ListView
)

from app.models import Lesson


class LessonListView(ListView):
    template_name = 'index.html'
    context_object_name = 'lessons'
    queryset = Lesson.objects.active()


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lesson.html'
    context_object_name = 'lesson'


class SubmitAnswerView(View):

    def post(self, request, course_slug, slug):
        form_data = json.loads(request.body.decode('utf-8').replace("'", '"'))
        # expected_code = Lesson.objects.filter(slug=slug).first().expectedanswer_set.first().expected_code

        response_data = {
            'data': form_data,
        }

        return JsonResponse(response_data)
