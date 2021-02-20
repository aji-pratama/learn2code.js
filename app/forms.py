from django import forms

from tinymce.widgets import TinyMCE

from app.models import Lesson


class LessonAdminForm(forms.ModelForm):
    instruction = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Lesson
        exclude = []
