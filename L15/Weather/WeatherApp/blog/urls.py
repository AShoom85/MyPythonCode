from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about_weather1/', views.about_weather1),
    path('about_weather2/', views.about_weather2),
    path('about_weather3/', views.about_weather3),
]
