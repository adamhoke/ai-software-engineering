from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ToDoList, ToDoItem

# For ToDoList
class ToDoListView(ListView):
    model = ToDoList
    template_name = 'todolist.html'

class ToDoListCreateView(CreateView):
    model = ToDoList
    fields = ['title']
    template_name = 'todolist_form.html'
    success_url = '/todo/'  # Redirect to todo list after creating

class ToDoListDetailView(UpdateView):
    model = ToDoList
    fields = ['title']
    template_name = 'todolist_detail.html'
    success_url = '/todo/'  # Redirect to todo list after updating

class ToDoListUpdateView(UpdateView):
    model = ToDoList
    fields = ['title']
    template_name = 'todolist_form.html'
    success_url = '/todo/'  # Redirect to todo list after updating

class ToDoListDeleteView(DeleteView):
    model = ToDoList
    template_name = 'todolist_confirm_delete.html'
    success_url = '/todo/'  # Redirect to todo list after deletion

# For ToDoItem
class ToDoItemView(ListView):
    model = ToDoList
    template_name = 'todoitem.html'

class ToDoItemCreateView(CreateView):
    model = ToDoItem
    fields = ['title', 'description', 'due_date', 'todolist']
    template_name = 'todoitem_form.html'
    success_url = '/todo/'  # Redirect to todo list after creating

class ToDoListDetailView(UpdateView):
    model = ToDoList
    fields = ['title']
    template_name = 'todoitem_detail.html'
    success_url = '/todo/'  # Redirect to todo list after updating

class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    fields = ['title', 'description', 'due_date', 'todolist']
    template_name = 'todoitem_form.html'
    success_url = '/todo/'  # Redirect to todo list after updating

class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    template_name = 'todoitem_confirm_delete.html'
    success_url = '/todo/'  # Redirect to todo list after deletion