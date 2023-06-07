from django.db import models


class Styles(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    styles = models.ManyToManyField(Styles, related_name='artists')

    def __str__(self):
        return self.first_name


class Photo(models.Model):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.artist)
