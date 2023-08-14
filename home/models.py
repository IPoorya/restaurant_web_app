from django.db import models
from django.urls import reverse
from accounts.models import User
import hashlib


def hash_function(input_string):
    hash_object = hashlib.md5(input_string.encode())
    hex_digest = hash_object.hexdigest()
    # Convert hexadecimal digest to decimal number
    hashed_number = int(hex_digest, 16)
    # Get last 8 digits of the hashed number
    return str(hashed_number % (10 ** 8))


class Category(models.Model):
    name = models.CharField(max_length=255)
    foods_number = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['id']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='food_images/')
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='foods')
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    sells = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Order(models.Model):
    order_token = models.PositiveIntegerField(null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='order')
    items = models.ManyToManyField(Food)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.order_token)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.order_token = hash_function(str(self.id) + ' : ' + self.user.name)
        for price in self.items.values_list('price', flat=True):
            self.price += price
        return super().save(*args, **kwargs)
