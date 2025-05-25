from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homework/', views.homework_view),
    path('homework/<int:pk>/', views.homework_id_view),
    path('dashboard/', views.dashboard, name='dashboard'),
]
