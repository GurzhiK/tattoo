from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=10000)

    def __str__(self):
        return self.first_name
