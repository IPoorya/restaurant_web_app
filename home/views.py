from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import redirect, render
from django.views import View
from .models import Food, Category
from django. contrib import messages
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
from .serializers import OrderSerializer


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
            })
        return render(request, 'home/home.html', {
            'foods': foods,
            'categories': categories,
        })


class HomeAPIView(APIView):

    def dispatch(self, request, *args, **kwargs):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            return super().dispatch(request, *args, **kwargs)

        return HttpResponseBadRequest('Invalid request')

    def post(self, request):
        data = request.data
        order = {
            "items": [],
            "price": 0,
            "name": '',
            "phone_number": '',
            "postal_code": '',
            "address": ''
        }
        seen = []
        count = []
        for d in data:
            food_name = d.split("[")[0]
            if d == "name":
                order['name'] = data[d]
            elif d == "phone_number":
                order['phone_number'] = data[d]
            elif d == "postal_code":
                order['postal_code'] = data[d]
            elif d == "address":
                order['address'] = data[d]
            else:
                if '[count]' in d:
                    count.append(data[d])
                    order['price'] += Food.objects.get(name=food_name).price * \
                        int(data[d]) * 10

                if d != "total" and d.split('[count]')[0] not in seen and d.split('[price]')[0] not in seen:
                    order['items'].append(Food.objects.get(name=food_name).id)
                    seen.append(food_name)

        order = OrderSerializer(data=order)
        if order.is_valid():
            order.save()

        return Response({'message': 'message recieved!'})
