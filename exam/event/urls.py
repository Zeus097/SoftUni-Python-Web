from django.urls import path, include
from event import views

urlpatterns = [
    path('', views.EventDetailsView.as_view(), name='events-details'),
    path('create/', views.EventCreateView.as_view(), name='events-create'),
    path('<int:id>/', include([
        path('details/', views.CurrentEventDetailsView.as_view(), name='current-event-details'),
        path('edit/', views.EventEditView.as_view(), name='current-event-edit'),
        path('delete/', views.EventDeleteView.as_view(), name='current-event-delete'),
    ]))
]


