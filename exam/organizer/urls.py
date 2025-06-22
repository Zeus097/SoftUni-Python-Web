from django.urls import path, include
from organizer import views

urlpatterns = [
    path('create/', views.OrganizerCreateView.as_view(), name='create-organizer'),
    path('details/', views.OrganizerDetailView.as_view(), name='details-organizer'),
    path('edit/', views.OrganizerEditView.as_view(), name='edit-organizer'),
    path('delete/', views.OrganizerDeleteView.as_view(), name='delete-organizer'),
]
