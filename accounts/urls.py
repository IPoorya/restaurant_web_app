from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('accounts/signup/', views.signup.as_view(), name='signup'),
    path('accounts/verify/', views.verifyCodeView.as_view(), name='verify_code'),
    path('accounts/login/', views.loginView.as_view(), name='login'),
    path('accounts/logout/', views.logoutView.as_view(), name='logout'),
]
