from django.shortcuts import render
from .models import Photography, Category
from .serializers import PhotographySerializer, CategorySerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class PhotographyList(generics.ListAPIView):
    queryset = Photography.objects.all()
    serializer_class = PhotographySerializer
    filter_backends = [filters.OrderingFilter,
                       DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']


class PhotographyDetail(generics.RetrieveAPIView):
    queryset = Photography.objects.all()
    serializer_class = PhotographySerializer


class PhotographyUpdate(generics.RetrieveUpdateAPIView):
    queryset = Photography.objects.all()
    serializer_class = PhotographySerializer


class PhotographyCreate(generics.CreateAPIView):
    queryset = Photography.objects.all()
    serializer_class = PhotographySerializer


class PhotographyDelete(generics.DestroyAPIView):
    queryset = Photography.objects.all()
    serializer_class = PhotographySerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDelete(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
