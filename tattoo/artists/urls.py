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
]
