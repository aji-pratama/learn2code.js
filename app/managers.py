from django.db import models


class ActiveManagerInteface(models.Manager):

    def active(self):
        return self.get_queryset().filter(active=True)


class StaticManagerInteface(models.Manager):

    def css(self):
        return self.get_queryset().filter(static_type=1)

    def html(self):
        return self.get_queryset().filter(static_type=2)

    def js(self):
        return self.get_queryset().filter(static_type=3)
