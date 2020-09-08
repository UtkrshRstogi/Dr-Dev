from django.urls import path

from login_functionality import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
]
