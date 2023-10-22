from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ToDoList, ToDoItem
from .forms import ToDoItemForm
from django.shortcuts import get_object_or_404
from django.urls import reverse

# For ToDoList
class ToDoListView(ListView):
    model = ToDoList
    template_name = 'todolist.html'

class ToDoListCreateView(CreateView):
    model = ToDoList
    fields = ['title']
    template_name = 'todolist_form.html'
    success_url = '/todo/lists'  # Redirect to todo list after creating

class ToDoListDetailView(DetailView):
    model = ToDoList
    fields = ['title']
    template_name = 'todolist_detail.html'
    success_url = '/todo/lists'  # Redirect to todo list after updating

class ToDoListUpdateView(UpdateView):
    model = ToDoList
    fields = ['title']
    template_name = 'todolist_form.html'
    success_url = '/todo/lists'  # Redirect to todo list after updating

class ToDoListDeleteView(DeleteView):
    model = ToDoList
    template_name = 'todolist_confirm_delete.html'
    success_url = '/todo/lists'  # Redirect to todo list after deletion

# For ToDoItem
class ToDoItemView(ListView):
    model = ToDoItem
    fields = ['title']
    template_name = 'todoitem.html'

class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemForm
    template_name = 'todoitem_form.html'
    
    def get_success_url(self):
        # Redirect to the ToDoListDetailView of the ToDoList the item belongs to
        return reverse('todolist_detail', args=[self.object.todolist.id])

class ToDoItemDetailView(DetailView):
    model = ToDoItem
    fields = ['title', 'description']
    template_name = 'todoitem_detail.html'

    def get_success_url(self):
        # Redirect to the ToDoListDetailView of the ToDoList the item belongs to
        return reverse('todoitem_detail', args=[self.object.id])

class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    form_class = ToDoItemForm    
    template_name = 'todoitem_form.html'
    
    def get_success_url(self):
        # Redirect to the ToDoListDetailView of the ToDoList the item belongs to
        return reverse('todoitem_detail', args=[self.object.id])

class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    template_name = 'todoitem_confirm_delete.html'
    
    def get_success_url(self):
        # Redirect to the ToDoListDetailView of the ToDoList the item belongs to
        return reverse('todolist_detail', args=[self.object.todolist.id])

# View to mark a todo item as done or not done
def toggle_todo_done(request, pk):
    """Toggle the completion status of a ToDo item."""
    item = get_object_or_404(ToDoItem, pk=pk)
    item.is_done = not item.is_done
    item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
