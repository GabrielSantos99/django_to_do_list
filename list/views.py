from .models import Task
from django.views import generic
from django.urls import reverse_lazy
from django.utils import timezone
from .mixin import SuccessMessageMixin

class TaskListView(generic.ListView):
    model = Task
    template_name = "list/task_list.html"
    context_object_name = "tasks"

class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "list/task_detail.html"
    context_object_name = "task"

class TaskCreateView(SuccessMessageMixin, generic.CreateView):
    model = Task
    template_name = "list/task_create.html"
    fields = ['task_title', 'task_description', 'status', 'conclusion_date']
    success_url = reverse_lazy("task_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['created_date'] = timezone.now()
        return context

class TaskUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Task
    template_name = "list/task_update.html" 
    context_object_name = "task"
    fields = ['task_title', 'task_description', 'status', 'conclusion_date']
    success_url = reverse_lazy('task_list')

class TaskDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Task
    template_name = "list/task_delete.html"
    context_object_name = "task"
    success_url = reverse_lazy("task_list")