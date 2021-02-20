from django.db import models


class ActiveManagerInteface(models.Manager):

    def get_queryset(self):
        return super(ActiveManagerInteface, self).get_queryset()

    def active(self):
        return self.get_queryset().filter(active=True)
