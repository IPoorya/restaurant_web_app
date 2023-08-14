from django.shortcuts import redirect, render
from django.views import View
from .models import Food, Category
from django. contrib import messages


class home(View):
    def get(self, request):
        try:
            categories = Category.objects.values_list(
                'name', flat=True)  # getting all categories

            if request.GET.get('category'):
                category = Category.objects.get(
                    name=request.GET.get('category'))
            else:
                category = Category.objects.get(name='پیتزا')
            foods = Food.objects.filter(category=category).filter(
                available=True).order_by('sells')
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
        except Category.DoesNotExist:
            messages.error(request, 'خطا، دسته بندی پیدا نشد', 'danger')
            return render(request, 'home/home.html')
