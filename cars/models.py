# cars/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField(max_length=100)
    description = models.TextField()
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cars')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
