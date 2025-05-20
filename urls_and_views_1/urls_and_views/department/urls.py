from django.urls import path, re_path
from department import views

urlpatterns = [
    path('', views.home_page),
    re_path(r'^department/(?P<year>202[0-5]-\d{2}-\d{2})/$', views.show_departments_by_year),
    path('department/<int:id>', views.show_department_by_id),
    path('department/<str:name>', views.search_department_by_name),
    path('department/<slug:slug>', views.show_department_by_slug),
    path('department/<str:name>', views.show_department_by_name),

]
