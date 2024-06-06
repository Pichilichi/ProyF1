from rest_framework.serializers import ModelSerializer
from .models import Event

# Transform the model Event into JSON data
class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'