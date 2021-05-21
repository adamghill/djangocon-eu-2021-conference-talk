from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Todo, TodoSerializer


# Serves VueJS application
index_view = never_cache(TemplateView.as_view(template_name="index.html"))


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited.
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
