from django import forms
from app.models import Lesson

from tinymce.widgets import TinyMCE


class LessonAdminForm(forms.ModelForm):
    instruction = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Lesson
        exclude = []
