from django.contrib import admin
from django.urls import path,include
from hello import views

urlpatterns = [
    
    path('', views.SignupPage,name="SignupPage"),
    path('index',views.index,name="index"),
    path('LoginPage', views.LoginPage,name="LoginPage"),
    path('Logout', views.Logout,name="Logout"),
]