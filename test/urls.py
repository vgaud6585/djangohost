from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),
  path('main-page/', views.main_page),
  
  ]