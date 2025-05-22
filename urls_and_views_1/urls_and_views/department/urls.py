from django.urls import path, re_path
from department import views

urlpatterns = [
    path('', views.home_page),
    re_path(r'^department/(?P<year>202[0-5]-\d{2}-\d{2})/$', views.show_departments_by_year),
    path('department/<slug:department_slug>/', views.show_department_by_slug),
    path('department/', views.department_page),
    path('department/<int:department_id>/', views.show_department_by_id),
    path('department/<str:department_name>/', views.show_department_by_name),
]
