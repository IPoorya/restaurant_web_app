from django.contrib import admin
from .models import Category, Food
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

    def display_category(self, obj):
        url = reverse("admin:home_category_change", args=[obj.category.id])
        print(url)
        return format_html('<a href="{}">{}</a>', url, obj.category.name)
    display_category.short_description = 'category'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'foods_number']
    readonly_fields = ['foods_number']
    search_fields = ['name']
    inlines = [
        FoodInline,
    ]
