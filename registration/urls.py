from django.contrib import admin
from django.urls import path
from . import views

app_name = "registration"

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('account/', views.accountSettings, name='account'),
]