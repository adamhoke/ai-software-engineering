### Phase Task:

For this application we want to be able to test the code that was written. We're going to assume a scenario where the devlopers have never really did a lot of testings and we'll need to get some feedback on how to write and run unit tests

### LLM Tool:

We're going to choose Google Bard for this, since we want to search and evaluate unit testing frameworks and get the latest instructions to run them.

### Prompt Pattern:

Persona pattern since we will be looking for expert advice

### Exact Input:

```
Act as a professional python developer. You have finished a Django web application and need to test it. List the best unit testing framework to use and which parts of a Django application you would generally write unit tests for. Also include instructions to run the unit tests.
```

### Exact Output:

```

Best unit testing framework for Django

Pytest is the most popular unit testing framework for Django. It is easy to use, flexible, and has a large community of users and contributors. Pytest also has a number of features that make it well-suited for testing Django applications, such as:

Support for fixtures, which allow you to easily set up and tear down test data.
Support for Django's built-in test client, which allows you to simulate HTTP requests to your application.
Integration with Django's test runner, which makes it easy to run your tests in a variety of environments.
Other popular unit testing frameworks for Django include:

Unittest, which is the standard unit testing framework included in Python.
Nose2, which is a fork of Nose, a popular older unit testing framework.
Testify, which is a newer unit testing framework that is gaining popularity.
Which parts of a Django application to write unit tests for

You should generally write unit tests for all of the following parts of a Django application:

Models - Unit tests for your models should ensure that they are correctly validating and saving data.
Views - Unit tests for your views should ensure that they are returning the correct responses to HTTP requests.
Forms - Unit tests for your forms should ensure that they are validating user input correctly.
Serializers - Unit tests for your serializers should ensure that they are correctly serializing and deserializing data.
Custom template tags and filters - Unit tests for your custom template tags and filters should ensure that they are working as expected.
Instructions to run unit tests with Pytest

To run unit tests with Pytest, you first need to install the Pytest package:
```

```bash
pip install pytest
```

```
Once you have installed Pytest, you can run your unit tests by executing the following command:
```

```bash
pytest
```

```
Pytest will automatically discover all of your test files and execute them. If any of your tests fail, Pytest will provide you with a detailed error report.

Here is an example of a simple Pytest unit test for a Django model:
```

```python
from django.test import TestCase
from .models import MyModel

class MyModelTest(TestCase):

    def test_create_my_model(self):
        my_model = MyModel(name='My Model')
        my_model.save()

        self.assertEqual(MyModel.objects.count(), 1)
        self.assertEqual(MyModel.objects.get().name, 'My Model')
```

```
To run this test, you would simply execute the following command:
```

```bash
pytest tests/my_model_test.py
```

```
If the test passes, Pytest will print a message saying "PASSED". If the test fails, Pytest will print a detailed error report.

You can also use Pytest to run unit tests for your views, forms, serializers, and custom template tags and filters. For more information, please see the Pytest documentation.
```

### Usage Result:

PyTest will be the framework to use and it seems even though the code is pretty straight forward we are going to test the models and views at least.