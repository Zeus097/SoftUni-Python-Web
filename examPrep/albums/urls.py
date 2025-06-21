from django.urls import path, include
from albums import views

urlpatterns = [
    path('add/', views.AlbumCreateView.as_view(), name='create_album'),
    path('<int:id>/details', include([
        path('details/', views.AlbumDetailsView.as_view(), name='album_details'),
        # path('edit', views.EditAlbum.as_view(), name=''),
        # path('delete', views.DeleteAlbum.as_view(), name=''),
    ])),
]
