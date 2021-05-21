from django.db import models
from rest_framework import serializers


class Todo(models.Model):
    task = models.CharField(max_length=1024)


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = (
            "pk",
            "task",
        )
