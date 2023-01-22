from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.home, name="home" ),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('login', views.loginuser, name="loginuser"),
    path('welcome', views.welcome, name="welcome"),
    path('register', views.register, name="register"),
    path('owner', views.owner, name="owner"),
]
