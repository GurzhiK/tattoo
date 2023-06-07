from django.db import models


class Category_service(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category_service, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
