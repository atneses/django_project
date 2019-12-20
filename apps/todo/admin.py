from django.contrib import admin
from apps.todo import models

# Register your models here.
@admin.register(models.TodoElement)
class TodoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.TodoList)
class TodoList(admin.ModelAdmin):
    pass