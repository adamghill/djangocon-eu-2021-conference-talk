from django.views.generic.base import TemplateView

from todo.models import Todo


class TodoView(TemplateView):
    template_name = "todo.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["todos"] = Todo.objects.all()

        return context
