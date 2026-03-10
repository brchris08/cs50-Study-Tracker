from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("log-session/", views.log_session, name="log_session"),
    path('edit/<int:pk>/', views.edit_session, name='edit_session'),
    path('delete/<int:pk>/', views.delete_session, name='delete_session'),
]