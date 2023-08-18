from django.shortcuts import redirect, render
from django.views import View
from .models import Food, Category
from django. contrib import messages


class home(View):
    def get(self, request):
        categories = Category.objects.values_list(
            'name', flat=True)  # getting all categories

        foods = Food.objects.filter(available=True).order_by('sells')
        if not foods:
            messages.error(request, 'موردی وجود ندارد', 'danger')
            return render(request, 'home/home.html', {
                'categories': categories,
                'button': request.GET.get('category') if request.GET.get('category') else 'پیتزا'
            })
        return render(request, 'home/home.html', {
            'foods': foods,
            'categories': categories,
            'button': request.GET.get('category') if request.GET.get('category') else 'پیتزا'
        })
