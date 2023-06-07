from django.shortcuts import render
from .models import Service, Price
from .serializers import ServiceSerializer, PriceSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [filters.OrderingFilter,
                       DjangoFilterBackend, filters.SearchFilter]
    ordering_fields = ['name']
    ordering = ['name']


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


class PriceList(generics.ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    filter_backends = [filters.OrderingFilter,
                       DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['service']
    ordering_fields = ['amount']
    ordering = ['amount']


class PriceDetail(generics.RetrieveAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceUpdate(generics.RetrieveUpdateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceCreate(generics.CreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceDelete(generics.DestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
