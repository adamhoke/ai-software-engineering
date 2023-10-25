## Sprint 1 - Design and Setup:

### Prerequisites

In a Django project, there are a number of commands to run that will generate a skeleton application and files that will run your basic application. This is a feature that has made Django the most popular web framework for the python programming language. We will also need to run some commands to activate the virtual environment, install the dependencies, and create the `requirements.txt` file that will be copied into and ran inside the application container.

- Initiate the virtual environment in the project. From inside the base directory run:

```
python3 -m venv .
```

- Create the empty requirements.txt file:

```
touch requirements.txt
```

- Install black and flake8:

```
pip install black && pip freeze > requirements.txt

pip install flake8 && pip freeze > requirements.txt
```

- Install Django (also save it to the requirements.txt file)

```
pip install django && pip freeze > requirements.txt
```

- Set up the Postgres backend. Since we are using the Docker Compose container, we should only have to install psycopg2-bin database adapter to get started:

```
pip install psycopg2-binary && pip freeze > requirements.txt
```

- Update the Django settings for the Postgres backend:

  - Navigate to todo_project/settings.py and make the following changes:

  ```python
  DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'tododb', 'USER': 'todouser', 'PASSWORD': 'todopassword', 'HOST': 'localhost', 'PORT': '5432', } }
  ```

- Start the Django parent “project” (a project can have many “apps” in Django but all apps need a parent to manage them):

```
django-admin startproject todo_project .
```

- Now that we’ve created the “app” we need to add it to the installed apps in the todo_project:

  - Navigate to todo_project/settings.py and add the app to the INSTALLED_APPS list:

  ```python
  INSTALLED_APPS = [ "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes", "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles", "todo_app", ]
  ```

- Create a directory named templates in the todo_app folder. Add a single file called base.html. Paste the following contents and save:

```html
<!-- todo_list/todo_app/templates/base.html -->

<!-- Base template -->

<!doctype html>

<html lang="en">

<head>

<!-- Required meta tags -->

<meta charset="utf-8">

<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Simple.css -->

<link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">

<title>Django To-do Lists</title>

</head>

<body>

<div>

<!-- When the title is clicked, it redirects to the index page -->

<h1 onclick="location.href='{% url "index" %}'">

Django To-do Lists

</h1>

</div>

<div>

<!-- This block will contain page-specific content, replaced in child templates -->

{% block content %}

This content will be replaced by different html code for each page.

{% endblock %}

</div>

</body>

</html>
```

- Test the activate.sh file by using it to start the virtual env:

```
source ./activate.sh
```

---------------------------------------------------------------------------------------

## Sprint 2 - Core Features Development:

### Phase Task:

We must implement the create, edit, and delete features of the to-do list and the todo-list items.


### LLM Tool:

ChatGPT-4 Code Interpreter for coding tasks.

### Prompt Pattern:

PQD pattern for coding tasks.

### Exact Input:

```
You are an expert python programmer. You are working on a Django web application with a Postgres backend called a “To-do List Application”.

Using the Django web framework, generate code to implement the create, edit, and delete features for a to-do list application. Here are the details:

Models:
 - ToDoList:
  - title (CharField, max_length=100, unique=True)
 - ToDoItem:
  - title (CharField, max_length=100)
  - description (TextField, can be null or blank)
  - created_date (DateTimeField, auto_now_add=True)
  - due_date (DateTimeField, default to one week from creation)
  - todolist (ForeignKey to ToDoList, on_delete=models.CASCADE)
  - is_done (BooleanField, default=False)
Views:
 - ToDoList:
  - Create: Use Django's CreateView with fields ['title'].
  - Edit: Use Django's UpdateView with fields ['title'].
  - Delete: Use Django's DeleteView.
 - ToDoItem:
  - Create: Use Django's CreateView with a form class containing fields for the ToDoItem.
  - Edit: Use Django's UpdateView with the same form class.
  - Delete: Use Django's DeleteView.
URLs:
 - ToDoList:
  - Create: lists/create/
  - Edit: lists/<int:pk>/update/
  - Delete: lists/<int:pk>/delete/
 - ToDoItem:
  - Create: items/create/
  - Edit: items/<int:pk>/update/
  - Delete: items/<int:pk>/delete/

Also, include necessary imports and helper functions like one_week_hence to calculate the default value for the due_date of ToDoItem. The code must be fast. The functions must have a docstring in python Google docstring format. Comment each line of code. Provide a few different solutions and explain the rational behind each.
```

### Exact Output:

```
Certainly! Let's tackle this step by step.

Models
First, we'll create the models for ToDoList and ToDoItem.
```

```python
from django.db import models
import datetime

class ToDoList(models.Model):
    """
    Model representing a to-do list.
    
    Attributes:
        title (str): The title of the to-do list. Must be unique.
    """
    title = models.CharField(max_length=100, unique=True)
    # CharField is used to store character data with a required max_length.

class ToDoItem(models.Model):
    """
    Model representing a to-do item in a to-do list.
    
    Attributes:
        title (str): The title of the to-do item.
        description (str): A detailed description of the to-do item. Can be empty.
        created_date (datetime): The date and time when the to-do item was created.
        due_date (datetime): The date and time when the to-do item is due.
        todolist (ForeignKey): A foreign key to the ToDoList that this item belongs to.
        is_done (bool): A flag indicating whether the to-do item is done.
    """
    
    def one_week_hence():
        """Helper function to return a datetime value one week from now."""
        return datetime.datetime.now() + datetime.timedelta(weeks=1)
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # TextField is used for larger text data. blank and null allows it to be optional.
    created_date = models.DateTimeField(auto_now_add=True)
    # auto_now_add sets the date to now when the object is first created.
    due_date = models.DateTimeField(default=one_week_hence)
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    # CASCADE means if the referred ToDoList is deleted, this ToDoItem will also be deleted.
    is_done = models.BooleanField(default=False)
```

```
Views
For the views, we'll use Django's generic class-based views: CreateView, UpdateView, and DeleteView.

ToDoList Views
```

```python
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ToDoList, ToDoItem
from .forms import ToDoItemForm  # We'll define this form later for ToDoItem views.

class ToDoListCreate(CreateView):
    """
    View to create a new to-do list.
    
    Attributes:
        model (Model): The model for this view.
        fields (list): List of fields to be used in the form.
    """
    model = ToDoList
    fields = ['title']

class ToDoListUpdate(UpdateView):
    """
    View to update an existing to-do list.
    
    Attributes:
        model (Model): The model for this view.
        fields (list): List of fields to be used in the form.
    """
    model = ToDoList
    fields = ['title']

class ToDoListDelete(DeleteView):
    """
    View to delete an existing to-do list.
    
    Attributes:
        model (Model): The model for this view.
        success_url (str): URL to redirect to after successful deletion.
    """
    model = ToDoList
    success_url = reverse_lazy('todolist-list')
    # reverse_lazy is used because URLs are not loaded when this file is imported, so we need a lazy version of reverse.
```

```
ToDoItem Views
For ToDoItem, we need to define a form first.
```

```python
from django import forms

class ToDoItemForm(forms.ModelForm):
    """
    Form for creating and updating ToDoItem objects.
    
    Attributes:
        model (Model): The model for this form.
        fields (list): List of fields to be included in the form.
    """
    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'due_date', 'todolist', 'is_done']

class ToDoItemCreate(CreateView):
    """
    View to create a new to-do item.
    
    Attributes:
        model (Model): The model for this view.
        form_class (ModelForm): The form class to be used.
    """
    model = ToDoItem
    form_class = ToDoItemForm

class ToDoItemUpdate(UpdateView):
    """
    View to update an existing to-do item.
    
    Attributes:
        model (Model): The model for this view.
        form_class (ModelForm): The form class to be used.
    """
    model = ToDoItem
    form_class = ToDoItemForm

class ToDoItemDelete(DeleteView):
    """
    View to delete an existing to-do item.
    
    Attributes:
        model (Model): The model for this view.
        success_url (str): URL to redirect to after successful deletion.
    """
    model = ToDoItem
    success_url = reverse_lazy('todoitem-list')
```

```
URLs
```

```python
from django.urls import path
from .views import ToDoListCreate, ToDoListUpdate, ToDoListDelete, ToDoItemCreate, ToDoItemUpdate, ToDoItemDelete

urlpatterns = [
    # ToDoList URLs
    path('lists/create/', ToDoListCreate.as_view(), name='todolist-create'),
    path('lists/<int:pk>/update/', ToDoListUpdate.as_view(), name='todolist-update'),
    path('lists/<int:pk>/delete/', ToDoListDelete.as_view(), name='todolist-delete'),

    # ToDoItem URLs
    path('items/create/', ToDoItemCreate.as_view(), name='todoitem-create'),
    path('items/<int:pk>/update/', ToDoItemUpdate.as_view(), name='todoitem-update'),
    path('items/<int:pk>/delete/', ToDoItemDelete.as_view(), name='todoitem-delete'),
]
```

```
Rationale:
Django's Class-Based Views (CBVs): We utilized CBVs because they provide a clean and reusable way to implement common CRUD operations, reducing the amount of code required.
Forms: For ToDoItem, a form was defined to ensure all required fields are present when creating or updating. This allows for better validation and customization.
URLs: The provided URL patterns follow RESTful conventions and allow for easy identification and routing to the appropriate views.
Alternative Approach:
One could also use Django's Function-Based Views (FBVs) instead of CBVs. FBVs are more flexible and allow for more granular control of the request-response cycle, but for basic CRUD operations, CBVs are usually more concise.

Another option would be to use Django Rest Framework (DRF) if building an API for the application.

The choice between these approaches would depend on the specific requirements of the project and the developer's familiarity with the frameworks.
```

### Usage Result:

We used this result, and will continue to add onto it in the next sprint. 

### File:

`todo_app/views.py`, `todo_app/models.py`, and `todo_app/urls.py`


---------------------------------------------------------------------------------------

## Sprint 3 - Advanced Features Development:

### Phase Task:

We must create the HTML templates that will support the backend code we've created so far

### LLM Tool:

ChatGPT-4 Code Interpreter for coding tasks.

### Prompt Pattern:

PQD pattern for coding tasks.

### Exact Input:

```
You are an expert python programmer. You are working on a Django web application with a Postgres backend called a “To-do List Application”. Create HTML templates suitable for a Django TodoList application, taking into consideration the following views and functionalities:

Templates for ToDoList:
 - ListView (URL: lists/)
  - Display a list of all ToDoLists.
  - Each ToDoList title should be clickable and redirect to its DetailView.
  - Include buttons/links for creating a new ToDoList, editing an existing ToDoList, and deleting an existing ToDoList.
 - CreateView & UpdateView (URLs: lists/create/ and lists/<int:pk>/update/)
  - Display a form with a field for the ToDoList title.
  - Include a submit button to save the ToDoList.
  - For UpdateView, pre-fill the form with the current data.
 - DeleteView (URL: lists/<int:pk>/delete/)
  - Display a confirmation message asking if the user is sure they want to delete the ToDoList.
  - Include confirm and cancel buttons.
Templates for ToDoItem:
 - ListView (URL: items/)
  - Display a list of all ToDoItems.
  - Each ToDoItem title should be clickable and redirect to its DetailView.
  - Display related information like description, created date, due date, and completion status.
  - Include buttons/links for marking a ToDoItem as done/not done, creating a new ToDoItem, editing an existing ToDoItem, and deleting an existing ToDoItem.
 - DetailView (URL: items/<int:pk>/)
  - Display details of the selected ToDoItem, including title, description, created date, due date, and completion status.
  - Include buttons/links for marking the ToDoItem as done/not done, editing, and deleting the ToDoItem.
 - CreateView & UpdateView (URLs: items/create/ and items/<int:pk>/update/)
  - Display a form with fields for the ToDoItem title, description, due date, and associated ToDoList.
  - Include a submit button to save the ToDoItem.
  - For UpdateView, pre-fill the form with the current data.
 - DeleteView (URL: items/<int:pk>/delete/)
  - Display a confirmation message asking if the user is sure they want to delete the ToDoItem.
  - Include confirm and cancel buttons. 
  
For all templates, ensure a consistent and user-friendly design. Incorporate any necessary Bootstrap or CSS for styling.Also, include necessary imports and helper functions like one_week_hence to calculate the default value for the due_date of ToDoItem. The code must be fast. The functions must have a docstring in python Google docstring format. Comment each line of code. Provide a few different solutions and explain the rational behind each.
```

### Exact Output:

```
Alright, let's create the templates for the ToDoList application. We will utilize Django's templating engine with Bootstrap for styling.

Base Template (base.html)
This template will serve as the foundation for all other templates, ensuring a consistent design.
```

```html
{% comment %} Load Bootstrap CSS and JS for styling and interactivity. {% endcomment %}
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django ToDoList Application</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
<div class="container mt-5">
    {% block content %}
    {% endblock %}
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

```
Templates for ToDoList
ListView (todolist_list.html)
Display all ToDoLists with options to create, edit, or delete.
```

```html
{% extends 'base.html' %}

{% block content %}
<h2>ToDo Lists</h2>
<ul class="list-group">
    {% for todolist in object_list %}
    <li class="list-group-item">
        <a href="{% url 'todolist-detail' todolist.pk %}">{{ todolist.title }}</a>
        <a href="{% url 'todolist-update' todolist.pk %}" class="btn btn-primary btn-sm">Edit</a>
        <a href="{% url 'todolist-delete' todolist.pk %}" class="btn btn-danger btn-sm">Delete</a>
    </li>
    {% endfor %}
</ul>
<a href="{% url 'todolist-create' %}" class="btn btn-success mt-3">Create New List</a>
{% endblock %}
```

```
CreateView & UpdateView (todolist_form.html)
Form for creating or updating a ToDoList.
```

```html
{% extends 'base.html' %}

{% block content %}
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Save</button>
</form>
{% endblock %}
```

```
DeleteView (todolist_confirm_delete.html)
Confirmation for deleting a ToDoList.
```

```html
{% extends 'base.html' %}

{% block content %}
<p>Are you sure you want to delete the list "{{ object.title }}"?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">Confirm</button>
    <a href="{% url 'todolist-list' %}" class="btn btn-secondary">Cancel</a>
</form>
{% endblock %}
```

```
Templates for ToDoItem
ListView (todoitem_list.html)
Display all ToDoItems with related information.
```

```html
{% extends 'base.html' %}

{% block content %}
<h2>ToDo Items</h2>
<table class="table table-bordered">
    <thead>
    <tr>
        <th>Title</th>
        <th>Description</th>
        <th>Created Date</th>
        <th>Due Date</th>
        <th>Status</th>
        <th>Actions</th>
    </tr>
    </thead>
    <tbody>
    {% for todoitem in object_list %}
    <tr>
        <td><a href="{% url 'todoitem-detail' todoitem.pk %}">{{ todoitem.title }}</a></td>
        <td>{{ todoitem.description }}</td>
        <td>{{ todoitem.created_date }}</td>
        <td>{{ todoitem.due_date }}</td>
        <td>{{ todoitem.is_done|yesno:"Done,Not Done" }}</td>
        <td>
            <a href="{% url 'todoitem-update' todoitem.pk %}" class="btn btn-primary btn-sm">Edit</a>
            <a href="{% url 'todoitem-delete' todoitem.pk %}" class="btn btn-danger btn-sm">Delete</a>
        </td>
    </tr>
    {% endfor %}
    </tbody>
</table>
<a href="{% url 'todoitem-create' %}" class="btn btn-success mt-3">Create New Item</a>
{% endblock %}
```

```
DetailView (todoitem_detail.html)
Display detailed information for a single ToDoItem.
```

```html
{% extends 'base.html' %}

{% block content %}
<h2>{{ object.title }}</h2>
<p><strong>Description:</strong> {{ object.description }}</p>
<p><strong>Created Date:</strong> {{ object.created_date }}</p>
<p><strong>Due Date:</strong> {{ object.due_date }}</p>
<p><strong>Status:</strong> {{ object.is_done|yesno:"Done,Not Done" }}</p>
<a href="{% url 'todoitem-update' object.pk %}" class="btn btn-primary">Edit</a>
<a href="{% url 'todoitem-delete' object.pk %}" class="btn btn-danger">Delete</a>
{% endblock %}
```

```
CreateView & UpdateView (todoitem_form.html)
Form for creating or updating a ToDoItem.
```

```html
{% extends 'base.html' %}

{% block content %}
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Save</button>
</form>
{% endblock %}
```

```
DeleteView (todoitem_confirm_delete.html)
Confirmation for deleting a ToDoItem.
```

```html
{% extends 'base.html' %}

{% block content %}
<p>Are you sure you want to delete the item "{{ object.title }}"?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">Confirm</button>
    <a href="{% url 'todoitem-list' %}" class="btn btn-secondary">Cancel</a>
</form>
{% endblock %}
```

```
Rationale:
Bootstrap: Bootstrap is incorporated for quick and responsive design, making the application user-friendly.
Consistent Design: By using a base.html template and extending it in other templates, we ensure a consistent look across the application.
URL Naming Convention: The URL names like 'todolist-create', 'todolist-update', etc., are placeholders and should match with the names defined in the Django URL configuration.
Alternative Approach:
Modularity: We can further split the templates into smaller reusable components using Django's {% include 'template_name.html' %} tag. This would make the templates more modular and easier to maintain.
Styling: The styling provided here is basic, using Bootstrap. For a more customized look, one can utilize SCSS or other CSS frameworks.
JavaScript Interactivity: For a more dynamic user experience, one could integrate JavaScript libraries/frameworks like Vue.js, React, or Angular.
The choice between these approaches would depend on the specific requirements of the project and the developer's familiarity with the technologies.
```

### Usage Result:

We copied these html snippets into their respective files in the `todo_app/templates` directory and restarted the application to render them.

### Files:

`todo_app/templates/*.html`

---------------------------------------------------------------------------------------

## Sprint 4 - Additional Features:

### Phase Task:

We must add extra features of due date and the ability to mark the item as done. However, this was actually completed automatically by ChatGPT-4, so we are good for now and can skip to the testing sprint!

---------------------------------------------------------------------------------------

## Sprint 5 - Testing, Debugging, and Documentation:

### Phase Task:

We will defer this task content to the "Testing Phase" (see the testing directory).

---------------------------------------------------------------------------------------

## Sprint 6 - Deployment and Feedback

### Phase Task:

We will defer this task content to the "Testing Phase" (see the testing directory).
