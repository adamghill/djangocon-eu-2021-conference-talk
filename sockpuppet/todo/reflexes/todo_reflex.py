from sockpuppet.reflex import Reflex

from todo.models import Todo


class TodoReflex(Reflex):
    def new_task(self):
        task = self.element.attributes["value"]
        self.request.session["new_task"] = task

    def add_todo(self):
        task = self.request.session["new_task"]
        todo = Todo(task=task)
        todo.save()

    def cancel(self):
        self.request.session["new_task"] = ""
