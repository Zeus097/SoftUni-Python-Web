from django.urls import path
from books_api import views


urlpatterns = [
    # Empty url path for easy testing
    path('', views.ListBooksView.as_view(),),
    path('books/<int:id>', views.DetailBookView.as_view(),),
]

