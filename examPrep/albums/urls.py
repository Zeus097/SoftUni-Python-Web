from django.urls import path, include
from albums import views

urlpatterns = [
    path('add/', views.AlbumCreateView.as_view(), name='create_album'),
    path('<int:id>/details', include([
        path('details/', views.AlbumDetailsView.as_view(), name='album_details'),
        path('edit', views.AlbumEditView.as_view(), name='album_edit'),
        path('delete', views.AlbumDeleteView.as_view(), name='album_delete'),
    ])),
]
