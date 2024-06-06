from django.urls import path
from . import views

urlpatterns = [
    path('', views.getEvents),
    path('events/', views.getEvents),
    path('events/<str:pk>/', views.getEvent),
]

