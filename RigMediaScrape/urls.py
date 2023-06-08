from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reddit_data', views.reddit_data),
    path('runSpider', views.runSpider),
]