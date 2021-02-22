from django.db import models

from app.managers import ActiveManagerInteface
from app.utils import unique_slug_generator


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    updated = models.DateTimeField(auto_now=True, verbose_name='updated at')

    class Meta:
        abstract = True


class Lesson(BaseModel):
    OUTPUT_INTERFACE_CHOICES = [
        (1, 'Console'),
        (2, 'Web'),
    ]

    title = models.CharField(max_length=255)
    output_interface = models.PositiveSmallIntegerField(default=1, choices=OUTPUT_INTERFACE_CHOICES)
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

    def get_next_lesson(self):
        return self.__class__.objects.active().filter(display_order__gt=self.display_order).first()


class ExpectedAnswer(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    expected_code = models.TextField(blank=True)
    expected_output = models.TextField()

    def __str__(self):
        return self.expected_output
