from django.db import models

from app.managers import ActiveManagerInteface
from app.utils import unique_slug_generator


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    updated = models.DateTimeField(auto_now=True, verbose_name='updated at')

    class Meta:
        abstract = True


class Lesson(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    instruction = models.TextField()
    initial_code = models.TextField(blank=True)

    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    objects = ActiveManagerInteface()

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.display_order == 0:
            self.display_order = self.pk

        if not self.slug:
            self.slug = unique_slug_generator(self)

        super(Lesson, self).save(*args, **kwargs)


class ExpectedAnswer(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    expected_code = models.TextField(blank=True)
    expected_output = models.TextField()

    def __str__(self):
        return self.expected_output
