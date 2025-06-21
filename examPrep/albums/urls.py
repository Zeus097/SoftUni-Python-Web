from django.urls import path, include
from albums import views

urlpatterns = [
    path('add/', views.AlbumCreateView.as_view(), name='create_album'),
    # path('<pk:int>/details', views.DetailsAlbum.as_view(), name=''),
    # path('<pk:int>/edit', views.EditAlbum.as_view(), name='edit'),
    # path('<pk:int>/delete', views.DeleteAlbum.as_view(), name='delete'),
]
