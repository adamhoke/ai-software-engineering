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

We must implement the create, edit, and delete features of the to-do list.


### LLM Tool:


### Prompt Pattern:


### Exact Input:


### Exact Output:


### Usage Result:


---------------------------------------------------------------------------------------

## Sprint 3 - Advanced Features Development:

### Phase Task:

We must implement the create, edit, and delete features of the todo list items, and ensure they are attached to to-do lists.

### LLM Tool:


### Prompt Pattern:


### Exact Input:


### Exact Output:


### Usage Result:


---------------------------------------------------------------------------------------

## Sprint 4 - Additional Features:

### Phase Task:

We must add extra features of due date and the ability to mark the item as done.

### LLM Tool:


### Prompt Pattern:


### Exact Input:


### Exact Output:


### Usage Result:


---------------------------------------------------------------------------------------

## Sprint 5 - Testing, Debugging, and Documentation:

### Phase Task:

We will defer this task to the "Testing Phase" (see the testing directory).

---------------------------------------------------------------------------------------

## Sprint 6 - Deployment and Feedback

### Phase Task:

We will defer this task to the "Testing Phase" (see the testing directory).
