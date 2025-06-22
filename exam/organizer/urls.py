from django.urls import path, include
from organizer import views

urlpatterns = [
    path('create/', views.OrganizerCreateView.as_view(), name='create-organizer'),
]
