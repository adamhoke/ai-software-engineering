from django.urls import reverse
from todo_app.models import ToDoList

@pytest.mark.django_db
class TestToDoListView:
    """
    Test suite for the ToDoList views.
    """

    def test_to_do_list_view_get(self, client):
        """
        Test the GET request for ToDoListView.
        """
        response = client.get(reverse('todolist_list'))
        assert response.status_code == 200, "Should return a 200 OK status code"
        assert 'todolist.html' in [t.name for t in response.templates], "Should use the correct template"

    def test_to_do_list_create_view_get(self, client):
        """
        Test the GET request for ToDoListCreateView.
        """
        response = client.get(reverse('todolist_create'))
        assert response.status_code == 200, "Should return a 200 OK status code"
        assert 'todolist_form.html' in [t.name for t in response.templates], "Should use the correct template"

    def test_to_do_list_create_view_post(self, client):
        """
        Test the POST request for ToDoListCreateView.
        """
        response = client.post(reverse('todolist_create'), {'title': 'New List'})
        assert response.status_code == 302, "Should redirect after successful creation"
        assert ToDoList.objects.filter(title='New List').exists(), "New ToDoList should be created"
