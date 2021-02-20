import json

from django.http import JsonResponse
from django.views.generic import (
    View,
    DetailView,
    ListView
)

from app.models import Learn


class LearnListView(ListView):
    template_name = 'index.html'
    context_object_name = 'learns'
    queryset = Learn.objects.active()


class LearnDetailView(DetailView):
    model = Learn
    template_name = 'learn.html'
    context_object_name = 'learn'


class SubmitAnswerView(View):

    def post(self, request, course_slug, slug):
        form_data = json.loads(request.body.decode('utf-8').replace("'", '"'))
        expected_code = Learn.objects.filter(slug=slug).first().expectedanswer_set.first().expected_code
        get_answer_code = sandbox(form_data['answer_code'])
        get_expected_code = sandbox(expected_code)

        is_correct = False
        if get_answer_code == get_expected_code:
            is_correct = True

        response_data = {
            'is_correct': is_correct,
            'answer_result': get_answer_code['result']
        }

        return JsonResponse(response_data)
