from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('artists/', ArtistList.as_view(), name='artist-list'),
    path('artists/detail/<int:pk>/',
         ArtistDetail.as_view(), name='artist-detail'),
    path('artists/create/',
         ArtistCreate.as_view(), name='artist-create'),
    path('artists/delete/<int:pk>/',
         ArtistDelete.as_view(), name='artist-delete'),
    path('artists/update/<int:pk>/',
         ArtistUpdate.as_view(), name='artist-update'),
    path('photos/', PhotoList.as_view(), name='photo-list'),
    path('prices/detail/<int:pk>/',
         PhotoDetail.as_view(), name='photo-detail'),
    path('photos/create/',
         PhotoCreate.as_view(), name='photo-create'),
    path('photos/delete/<int:pk>/',
         PhotoDelete.as_view(), name='photo-delete'),
    path('photos/update/<int:pk>/',
         PhotoUpdate.as_view(), name='photo-update'),
    path('styles/', StylesList.as_view(), name='style-list'),
    path('styles/detail/<int:pk>/',
         StylesDetail.as_view(), name='style-detail'),
    path('styles/create/',
         StylesCreate.as_view(), name='style-create'),
    path('styles/delete/<int:pk>/',
         StylesDelete.as_view(), name='style-delete'),
    path('styles/update/<int:pk>/',
         StylesUpdate.as_view(), name='style-update'),
]
