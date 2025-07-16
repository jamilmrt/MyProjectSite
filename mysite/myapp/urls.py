from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('create_project/', views.createProjectView, name='create_project'),
    path('list_item<int:pk>/', views.listItem, name='list_item'),
    path("<int:project_id>/edit/", views.project_edit, name="project_edit"),
    path("<int:project_id>/delete/", views.project_delete, name="project_delete"),
    
]