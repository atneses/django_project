from rest_framework import serializers, viewsets
from apps.todo import models

class TodoElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoElement
        fields = '__all__'


class CustomTodoElementFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoElement
        fields = ['id', 'title', 'description']

class TodoListSerializer(serializers.ModelSerializer):
    todos = CustomTodoElementFieldsSerializer(many=True)

    class Meta:
        model = models.TodoList
        fields = '__all__'

# ViewSets define the view behavior.
class TodoListViewSet(viewsets.ModelViewSet):
    queryset = models.TodoList.objects.all()
    serializer_class = TodoListSerializer

class TodoElementViewSet(viewsets.ModelViewSet):
    queryset = models.TodoElement.objects.all()
    serializer_class = TodoElementSerializer

