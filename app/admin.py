from django.contrib import admin

from app.models import Lesson, ExpectedAnswer
from app.forms import LessonAdminForm, ExpectedAnswerAdminForm


class ExpectedAnswerInline(admin.StackedInline):
    model = ExpectedAnswer
    form = ExpectedAnswerAdminForm
    extra = 1


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'display_order']
    inlines = [ExpectedAnswerInline]
    form = LessonAdminForm
