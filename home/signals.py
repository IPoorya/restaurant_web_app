from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Order


@receiver(m2m_changed, sender=Order.items.through)
def calculate_order_price(sender, instance, action, **kwargs):
    if action == 'post_add' or action == 'post_remove':
        price = 0
        for item in instance.items.all():
            price += item.price
        instance.price = price
        instance.save()
