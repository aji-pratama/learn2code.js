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
        # expected_code = Learn.objects.filter(slug=slug).first().expectedanswer_set.first().expected_code

        response_data = {
            'data': form_data,
        }

        return JsonResponse(response_data)
