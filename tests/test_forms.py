from todo_app.forms import ToDoItemForm
from todo_app.models import ToDoList

@pytest.mark.django_db
class TestToDoItemForm:
    """
    Test suite for the ToDoItemForm.
    """

    def test_to_do_item_form_valid_data(self):
        """
        Test the ToDoItemForm with valid data.
        """
        to_do_list = ToDoList.objects.create(title="Test List")
        form_data = {
            'title': 'Test Item',
            'description': 'Test Description',
            'due_date': '2023-11-10 12:00:00',
            'todolist': to_do_list.id,
            'is_done': False
        }
        form = ToDoItemForm(data=form_data)
        assert form.is_valid(), "Form should be valid with correct data"

    def test_to_do_item_form_invalid_data(self):
        """
        Test the ToDoItemForm with invalid data.
        """
        form_data = {
            'title': '',  # Empty title
            'description': 'Test Description',
            'due_date': '2023-11-10 12:00:00',
            'todolist': None,  # Missing ToDoList
            'is_done': False
        }
        form = ToDoItemForm(data=form_data)
        assert not form.is_valid(), "Form should be invalid with incorrect data"
        assert 'title' in form.errors, "Title field should have an error"
        assert 'todolist' in form.errors, "ToDoList field should have an error"

