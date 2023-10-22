from django import forms
from .models import ToDoItem

class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'due_date', 'is_done', 'todolist']

        # Modify the labels here
        labels = {
            'title': 'Task Title',
            'description': 'Task Details',
            'due_date': 'Completion Date',
            'is_done': 'Completed',
            'todolist': 'To-Do List'
        }
