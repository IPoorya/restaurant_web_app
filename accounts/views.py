from django.shortcuts import redirect, render
from django.views import View
from .forms import UserCreationForm


class signup(View):
    form_class = UserCreationForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/signup.html', {
            'form': form,
        })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect('home:home')

        return render(request, 'accounts/signup.html', {
            'form': form,
        })
