from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile, name='profile'),
    path('location/', views.location, name='location'),
    path('discover/', views.discover, name='discover'),
    path('payment/', views.payment, name='payment'),
    path('receipt/', views.receipt, name='receipt'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('login/', auth_view.LoginView.as_view(template_name = 'cab/login.html'), name = 'login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='cab/logout.html'), name='logout'),


]