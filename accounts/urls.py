from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('accounts/signup/', views.signup.as_view(), name='signup'),
    # path('accounts/login/', views.login.as_view(), name='login'),
]
