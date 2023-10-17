from django.urls import path
from .views import *

urlpatterns = [
    path('lists/', ToDoListView.as_view(), name='todolists'),
    path('lists/create/', ToDoListCreateView.as_view(), name='todolist-create'),
    path('lists/<int:pk>/', ToDoListDetailView.as_view(), name='todolist_detail'),    
    path('lists/<int:pk>/update/', ToDoListUpdateView.as_view(), name='todolist-update'),
    path('lists/<int:pk>/delete/', ToDoListDeleteView.as_view(), name='todolist-delete'),
    path('items/', ToDoItemView.as_view(), name='todoitems'),
    path('items/create/', ToDoItemCreateView.as_view(), name='todoitem-create'),
    path('items/<int:pk>/', ToDoItemDetailView.as_view(), name='todoitem_detail'),   
    path('items/<int:pk>/update/', ToDoItemUpdateView.as_view(), name='todoitem-update'),
    path('items/<int:pk>/delete/', ToDoItemDeleteView.as_view(), name='todoitem-delete'),
    path('items/<int:pk>/toggle_done/', toggle_todo_done, name='todoitem-toggle_done'),
]
