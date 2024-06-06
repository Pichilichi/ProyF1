from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event

@api_view(['GET'])
def getEvents(request):
    routes = [
        {
            'Endpoint': '/events/',
            'method': 'GET',
            'body': None,
            'description': 'Returns events'
        },
        {
            'Endpoint': '/events/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single event'
        },
        {
            'Endpoint': '/events/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Create event'
        },
        {
            'Endpoint': '/events/id/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Update event'
        },
        {
            'Endpoint': '/events/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete event'
        },
    ]

    return Response(routes)

# All events
@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True) # Many = true for everything, false if only one
    return Response(serializer.data)