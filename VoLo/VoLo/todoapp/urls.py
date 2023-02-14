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
    path('add', views.add, name="add"),
    path('delete/<str:name>', views.delete, name="delete"),
    path('view/<str:obj>/<str:obj2>/<str:obj3>/<str:obj4>/<str:obj5>', views.view, name="view"),
    path('accept/<str:obj>/<str:obj2>/<str:obj3>/<str:obj4>/<str:obj5>', views.accept, name="accept")

]
