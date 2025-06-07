from django.urls import path, include
from posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.list_of_departments_view, name='departments'),
    path('departments/', include([
        path('add/', views.add_department_view, name='add_department'),
        path('edit/<int:pk>/', views.edit_department_view, name='edit_department'),
        path('delete/<int:pk>/', views.delete_department_view, name='delete_department'),
        path('details/<int:pk>/', views.department_details_view, name='department_details'),
    ])),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('post/', include([
        path('add/', views.add_post, name='add-post'),
        path('edit/<int:pk>/', views.edit_post, name='edit-post'),
        path('delete/<int:pk>/', views.delete_post, name='delete-post'),
        path('details/<int:pk>', views.post_details, name='post-details')
    ])),
]
