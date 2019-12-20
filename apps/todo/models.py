from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Base(models.Model):
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class TodoElement(Base): 
    title = models.CharField(max_length=100)
    description = models.TextField()
    elements = models.ForeignKey('TodoList', related_name='todos', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Todo element'
        verbose_name_plural = 'Todo elements'
    def __str__(self):
        return self.title


class TodoList(Base):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Todo list'
        verbose_name_plural = 'Todo lists'