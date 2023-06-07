from django.shortcuts import render
from .models import Styles, Artist, Photo
from .serializers import StylesSerializer, PhotoSerializer, ArtistSerializer, StylesDetailSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class StylesList(generics.ListAPIView):
    queryset = Styles.objects.all()
    serializer_class = StylesSerializer


class StylesDetail(generics.RetrieveAPIView):
    queryset = Styles.objects.all()
    serializer_class = StylesDetailSerializer


class StylesUpdate(generics.RetrieveUpdateAPIView):
    queryset = Styles.objects.all()
    serializer_class = StylesSerializer


class StylesCreate(generics.CreateAPIView):
    queryset = Styles.objects.all()
    serializer_class = StylesSerializer


class StylesDelete(generics.DestroyAPIView):
    queryset = Styles.objects.all()
    serializer_class = StylesSerializer


class PhotoList(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoDetail(generics.RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoCreate(generics.CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoDelete(generics.DestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistUpdate(generics.RetrieveUpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistCreate(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDelete(generics.DestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
