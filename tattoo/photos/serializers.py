from .models import Photography, Category
from rest_framework import serializers


class PhotographySerializer(serializers.ModelSerializer):

    class Meta:
        model = Photography
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
