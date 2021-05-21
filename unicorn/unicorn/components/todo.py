from django_unicorn.components import UnicornView
from todo.models import Todo


class TodoView(UnicornView):
    task: str = ""
    todos = Todo.objects.none()

    def hydrate(self):
        self.todos = Todo.objects.all()

    def add_todo(self):
        todo = Todo(task=self.task)
        todo.save()

        self.task = ""
