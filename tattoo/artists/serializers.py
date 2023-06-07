from .models import Styles, Artist, Photo
from rest_framework import serializers


class StylesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Styles
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'


class StylesDetailSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True)

    class Meta:
        model = Styles
        fields = ('id', 'name', 'artists')
