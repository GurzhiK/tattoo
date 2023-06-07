from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('categorys/', CategoryList.as_view(), name='categorys-list'),
    path('categorys/detail/<int:pk>/',
         CategoryDetail.as_view(), name='category-detail'),
    path('categorys/create/',
         CategoryCreate.as_view(), name='category-create'),
    path('categorys/delete/<int:pk>/',
         CategoryDelete.as_view(), name='category-delete'),
    path('categorys/update/<int:pk>/',
         CategoryUpdate.as_view(), name='category-update'),
    path('photographys/', PhotographyList.as_view(), name='photography-list'),
    path('photographys/detail/<int:pk>/',
         PhotographyDetail.as_view(), name='photography-detail'),
    path('photographys/create/',
         PhotographyCreate.as_view(), name='photography-create'),
    path('photographys/delete/<int:pk>/',
         PhotographyDelete.as_view(), name='photography-delete'),
    path('photographys/update/<int:pk>/',
         PhotographyUpdate.as_view(), name='photography-update'),
]
