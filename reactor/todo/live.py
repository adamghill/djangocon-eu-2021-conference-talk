from reactor.component import Component

from todo.models import Todo


class XTodo(Component):
    template_name = "todo/x-todo.html"
    new_task = ""

    def mount(self, **kwargs):
        self.todos = Todo.objects.all()

    def receive_task(self, new_task, **kwargs):
        self.new_task = new_task

    def receive_add_todo(self, **kwargs):
        todo = Todo(task=self.new_task)
        todo.save()

        self.new_task = ""
        self.todos = Todo.objects.all()

    def receive_cancel(self, **kwargs):
        self.new_task = ""
