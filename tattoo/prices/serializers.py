from .models import Service, Category_service
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


class Category_serviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category_service
        fields = '__all__'
