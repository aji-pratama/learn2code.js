from django.contrib import admin

from app.models import Lesson, ExpectedAnswer, ExtraStatic
from app.forms import LessonAdminForm, ExpectedAnswerAdminForm


class ExpectedAnswerInline(admin.StackedInline):
    model = ExpectedAnswer
    form = ExpectedAnswerAdminForm
    extra = 1


class ExtraStaticInline(admin.TabularInline):
    model = ExtraStatic
    extra = 0


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'active', 'is_correct', 'display_order']
    list_editable = ['active', 'is_correct']
    inlines = [ExtraStaticInline, ExpectedAnswerInline]
    form = LessonAdminForm
