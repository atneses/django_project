from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Base(models.Model):
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True
