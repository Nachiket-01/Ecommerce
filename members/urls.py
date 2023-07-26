from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('home/', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginview, name='login'),
    path('signup/', views.signup, name='signup'),
    path('password-update/', views.password_update, name='password_update'),

]