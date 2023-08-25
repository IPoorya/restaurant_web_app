from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import redirect, render
from django.views import View
from .models import Food, Category, Order
from django. contrib import messages
from rest_framework.response import Response
import json
from django.http import JsonResponse, HttpResponseBadRequest


class home(View):
    def get(self, request):
        categories = Category.objects.values_list(
            'name', flat=True)  # getting all categories

        foods = Food.objects.filter(available=True).order_by(
            'sells')  # getting all the available foods

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


class HomeAPIView(APIView):

    def dispatch(self, request, *args, **kwargs):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            return super().dispatch(request, *args, **kwargs)

        return HttpResponseBadRequest('Invalid request')

    def post(self, request):
        data = request.data
        print(data)

        return Response({'message': 'message recieved!'})
