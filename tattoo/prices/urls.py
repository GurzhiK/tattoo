from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('services/', ServiceList.as_view(), name='service-list'),
    path('services/detail/<int:pk>/',
         ServiceDetail.as_view(), name='service-detail'),
    path('services/create/',
         ServiceCreate.as_view(), name='service-create'),
    path('services/delete/<int:pk>/',
         ServiceDelete.as_view(), name='service-delete'),
    path('services/update/<int:pk>/',
         ServiceUpdate.as_view(), name='service-update'),
    path('categorys/', Category_serviceList.as_view(), name='category-list'),
    path('categorys/detail/<int:pk>/',
         Category_serviceDetail.as_view(), name='category-detail'),
    path('categorys/create/',
         Category_serviceCreate.as_view(), name='category-create'),
    path('category/delete/<int:pk>/',
         Category_serviceDelete.as_view(), name='category-delete'),
    path('categorys/update/<int:pk>/',
         Category_serviceUpdate.as_view(), name='category-update'),
]
