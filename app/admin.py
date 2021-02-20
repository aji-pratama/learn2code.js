from django.contrib import admin

from app.models import Lesson, ExpectedAnswer
from app.forms import LessonAdminForm

admin.site.register(ExpectedAnswer)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    form = LessonAdminForm
