from rest_framework.serializers import ModelSerializer
from .models import *

# Transform the model Event into JSON data
class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
class KartSerializer(ModelSerializer):
    class Meta:
        model = Kart
        fields = '__all__'
        
class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
class ModifyBookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ["name", "circuit"]
        
class CircuitSerializer(ModelSerializer):
    class Meta:
        model = Circuit
        fields = '__all__'
        
class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
        
class ModifyEquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = ["name"]
        
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'