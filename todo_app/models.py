from django.db import models
from django.urls import reverse
import datetime

class ToDoList(models.Model):
    """ Model representing a ToDo List """
    
    title = models.CharField(max_length=100, unique=True)  # Title of the ToDo list, unique so no two lists have the same name
    
    def __str__(self):
        """ String representation of the ToDoList """
        return self.title
    
    def get_absolute_url(self):
        """ Returns the url to access a detail record for this ToDoList """
        return reverse('todolist_detail', args=[str(self.id)])

class ToDoItem(models.Model):
    """ Model representing a ToDo Item """
    
    title = models.CharField(max_length=100)  # Title of the ToDo item
    description = models.TextField(null=True, blank=True)  # Description of the ToDo item. Can be empty
    created_date = models.DateTimeField(auto_now_add=True)  # Date and time when the ToDo item was created
    due_date = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(weeks=1))  # Due date for the ToDo item, defaults to one week from creation
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)  # ForeignKey relationship to ToDoList with cascading delete
    is_done = models.BooleanField(default=False)  # Indicates whether the todo item is done or not
    
    def __str__(self):
        """ String representation of the ToDoItem """
        return self.title
    
    def get_absolute_url(self):
        """ Returns the url to access a detail record for this ToDoItem """
        return reverse('todoitem_detail', args=[str(self.id)])

