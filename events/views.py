from rest_framework.decorators import api_view
from rest_framework.response import Response

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