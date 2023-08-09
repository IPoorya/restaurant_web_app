from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    foods_number = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='food_images/')
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='foods')
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    sells = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.category.foods_number += 1
        self.category.save()
        return super().save(*args, **kwargs)
