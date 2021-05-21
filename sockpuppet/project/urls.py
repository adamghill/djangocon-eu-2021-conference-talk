from django.urls import path

from todo.views.todo import TodoView


urlpatterns = [
    path("", TodoView.as_view()),
]
