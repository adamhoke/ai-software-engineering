from django.contrib import admin
from .models import ToDoList, ToDoItem

# Register the models for the admin site
admin.site.register(ToDoList)
admin.site.register(ToDoItem)
