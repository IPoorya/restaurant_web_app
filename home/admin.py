from django.contrib import admin
from .models import Category, Food, Order
from django.urls import reverse
from django.utils.html import format_html


class FoodInline(admin.StackedInline):
    model = Food
    readonly_fields = ['sells']
    extra = 0


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_category', 'price',
                    'sells', 'created', 'available']
    readonly_fields = ['sells']
    search_fields = ['name']
    list_editable = ['available']

    def display_category(self, obj):
        url = reverse("admin:home_category_change", args=[obj.category.id])
        return format_html('<a href="{}">{}</a>', url, obj.category.name)
    display_category.short_description = 'category'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    inlines = [
        FoodInline,
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'order_token', 'date', 'price']
    readonly_fields = ['name', 'phone_number',
                       'postal_code', 'price', 'order_token', 'date']
    search_fields = ['order_token', 'name', 'postal_code', 'phone_number']
    # raw_id_fields = ['items']
