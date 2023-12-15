from django .urls import path

from todo_app import views
urlpatterns = [
    path('', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('cbv/', views.TaskListView.as_view(), name='cbv'),
    path('cbdv/<int:pk>/', views.TaskDetailView.as_view(), name='c'),
    path('cbuv/<int:pk>/', views.TaskUpdateView.as_view(), name='cbuv'),
    path('cbdv/<int:pk>/', views.DeleteView.as_view(), name='cbdv'),
]
