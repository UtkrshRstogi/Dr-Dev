from django.urls import path

from home import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact', views.contact),
]
