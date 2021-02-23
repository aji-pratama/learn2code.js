from django import forms

from app.models import Lesson, ExpectedAnswer
from app.widgets import CodeMirrorWidget, TinyMCEWidget


class LessonAdminForm(forms.ModelForm):
    instruction = forms.CharField(widget=TinyMCEWidget())
    initial_code = forms.CharField(widget=CodeMirrorWidget())

    class Meta:
        model = Lesson
        exclude = []


class ExpectedAnswerAdminForm(forms.ModelForm):
    expected_code = forms.CharField(widget=CodeMirrorWidget())

    class Meta:
        model = ExpectedAnswer
        exclude = []
