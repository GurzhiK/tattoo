from django.shortcuts import render
from .models import Service, Category_service
from .serializers import ServiceSerializer, Category_serviceSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceUpdate(generics.RetrieveUpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceCreate(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDelete(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class Category_serviceList(generics.ListAPIView):
    queryset = Category_service.objects.all()
    serializer_class = Category_serviceSerializer


class Category_serviceDetail(generics.RetrieveAPIView):
    queryset = Category_service.objects.all()
    serializer_class = Category_serviceSerializer


class Category_serviceUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category_service.objects.all()
    serializer_class = Category_serviceSerializer


class Category_serviceCreate(generics.CreateAPIView):
    queryset = Category_service.objects.all()
    serializer_class = Category_serviceSerializer


class Category_serviceDelete(generics.DestroyAPIView):
    queryset = Category_service.objects.all()
    serializer_class = Category_serviceSerializer
