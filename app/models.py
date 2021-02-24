from django.db import models

from app.managers import ActiveManagerInteface, StaticManagerInteface
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
        if not self.slug:
            self.slug = unique_slug_generator(self)

        super(Lesson, self).save(*args, **kwargs)

    def get_prev_lesson(self):
        return self.__class__.objects.active().filter(display_order__lt=self.display_order).first()

    def get_next_lesson(self):
        return self.__class__.objects.active().filter(display_order__gt=self.display_order).first()


class ExtraStatic(BaseModel):
    STATIC_CHOICES = [
        (1, 'CSS'),
        (2, 'HTML'),
        (3, 'Javascript'),
    ]
    lesson = models.ForeignKey(Lesson, related_name='extra_static', on_delete=models.CASCADE)
    static_type = models.PositiveSmallIntegerField(default=1, choices=STATIC_CHOICES)
    url = models.URLField(max_length=255, blank=True, null=True)
    script = models.TextField(blank=True)

    display_order = models.PositiveIntegerField(default=0, help_text='If the static assets need to order.')
    objects = StaticManagerInteface()

    class Meta:
        ordering = ['static_type', 'display_order']

    def __str__(self):
        return '{} extra {}'.format(self.lesson.title, self.get_static_type_display())


class ExpectedAnswer(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    expected_code = models.TextField(blank=True)

    def __str__(self):
        return self.lesson.title
