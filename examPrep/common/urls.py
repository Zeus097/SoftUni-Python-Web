from django.urls import path, include
from common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]
