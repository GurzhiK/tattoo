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
    path('prices/', PriceList.as_view(), name='service-list'),
    path('prices/detail/<int:pk>/',
         PriceDetail.as_view(), name='price-detail'),
    path('prices/create/',
         PriceCreate.as_view(), name='price-create'),
    path('prices/delete/<int:pk>/',
         PriceDelete.as_view(), name='price-delete'),
    path('prices/update/<int:pk>/',
         PriceUpdate.as_view(), name='price-update'),
]
