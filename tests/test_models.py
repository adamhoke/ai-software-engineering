import pytest
from django.urls import reverse
from todo_app.models import ToDoList

@pytest.mark.django_db
class TestToDoListModel:
    """
    Test suite for the ToDoList model.
    """

    def test_to_do_list_str(self):
        """
        Test the string representation of the ToDoList model.
        """
        to_do_list = ToDoList(title="Test List")
        assert str(to_do_list) == "Test List", "String representation should be the title of the ToDoList"

    def test_get_absolute_url(self):
        """
        Test the get_absolute_url method of the ToDoList model.
        """
        to_do_list = ToDoList.objects.create(title="Test List")
        assert to_do_list.get_absolute_url() == reverse('todolist_detail', args=[str(to_do_list.id)]), "get_absolute_url should return the correct URL for the ToDoList"


@pytest.mark.django_db
class TestToDoItemModel:
    """
    Test suite for the ToDoItem model.
    """

    def test_to_do_item_str(self):
        """
        Test the string representation of the ToDoItem model.
        """
        to_do_item = ToDoItem(title="Test Item")
        assert str(to_do_item) == "Test Item", "String representation should be the title of the ToDoItem"

    def test_get_absolute_url(self):
        """
        Test the get_absolute_url method of the ToDoItem model.
        """
        to_do_list = ToDoList.objects.create(title="Test List")
        to_do_item = ToDoItem.objects.create(
            title="Test Item",
            description="Test Description",
            due_date=datetime.datetime.now() + datetime.timedelta(weeks=1),
            todolist=to_do_list,
            is_done=False
        )
        assert to_do_item.get_absolute_url() == reverse('todoitem_detail', args=[str(to_do_item.id)]), "get_absolute_url should return the correct URL for the ToDoItem"

    def test_due_date_default(self):
        """
        Test the default value of due_date field of the ToDoItem model.
        """
        to_do_list = ToDoList.objects.create(title="Test List")
        to_do_item = ToDoItem.objects.create(
            title="Test Item",
            description="Test Description",
            todolist=to_do_list,
            is_done=False
        )
        assert to_do_item.due_date > datetime.datetime.now(), "Default due_date should be in the future"
        assert to_do_item.due_date < datetime.datetime.now() + datetime.timedelta(weeks=1, seconds=1), "Default due_date should be within one week from creation"