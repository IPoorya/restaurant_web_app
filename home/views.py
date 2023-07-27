from django.shortcuts import redirect, render
from django.views import View


class home(View):
    def get(self, request):
        return render(request, 'home/home.html')
