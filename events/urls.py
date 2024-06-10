from django.urls import path
from . import views

urlpatterns = [
    path('', views.getBookings),
    # path('events/', views.getEvents),
    # path('events/create/', views.createEvent),
    # path('events/<str:pk>/update/', views.updateEvent),
    # path('events/<str:pk>/delete/', views.deleteEvent),
    # path('events/<str:pk>/', views.getEvent),
    
    path('equipments/', views.getEquipments),
    path('equipments/<int:id>', views.getEquipmentDetail),
    
    path('bookings/', views.getBookings),
    path('bookings/<int:id>', views.getBookingsDetail),
    
    path('categories/', views.getCategories),
    path('categories/<int:id>', views.getCategoryDetail),
    
    path('circuits/', views.getCircuits),
    path('circuits/<int:id>', views.getCircuitDetail),
    
    path('karts/', views.getKarts),
    path('messages/', views.getMessages),
    
]

