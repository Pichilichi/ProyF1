from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status

# @api_view(['GET'])
# def getEvents(request):
#     routes = [
#         {
#             'Endpoint': '/events/',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns events'
#         },
#         {
#             'Endpoint': '/events/id',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns a single event'
#         },
#         {
#             'Endpoint': '/events/create',
#             'method': 'POST',
#             'body': {'body': ""},
#             'description': 'Create event'
#         },
#         {
#             'Endpoint': '/events/id/update',
#             'method': 'PUT',
#             'body': {'body': ""},
#             'description': 'Update event'
#         },
#         {
#             'Endpoint': '/events/id/delete',
#             'method': 'DELETE',
#             'body': None,
#             'description': 'Delete event'
#         },
#     ]

#     return Response(routes)

# # All events
# @api_view(['GET'])
# def getEvents(request):
#     events = Event.objects.all()
#     serializer = EventSerializer(events, many=True) # Many = true for everything, false if only one
#     return Response(serializer.data)

## EQUIPMENT ##

# ALL OF THEM
@api_view(['GET',  'POST'])
def getEquipments(request):
    
    if request.method == 'GET': #SEE
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True) # Many = true for everything, false if only one
        return Response(serializer.data)
    
    elif request.method == 'POST': #CREATE
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# DETERMINED BY ID
@api_view(['GET', 'PUT', 'DELETE'])        
def getEquipmentDetail(request, id):
    
    try:
        equipment = Equipment.objects.get(pk=id)
    except Equipment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': #SEE
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data)
    
    elif request.method == 'PUT': #UPDATE
        serializer = ModifyEquipmentSerializer(equipment, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': #DELETE
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

## BOOKINGS ##

# ALL OF THEM
@api_view(['GET', 'POST'])
def getBookings(request):
    if request.method == 'GET': #SEE
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True) # Many = true for everything, false if only one
        return Response(serializer.data)
    
    elif request.method == 'POST': #CREATE
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
 
# DETERMINED BY ID       
@api_view(['GET', 'PUT', 'DELETE'])        
def getBookingsDetail(request, id):
    
    try:
        booking = Booking.objects.get(pk=id)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': #SEE
        serializer = BookingSerializer(booking)
        return Response(serializer.data)
    
    elif request.method == 'PUT': #UPDATE
        serializer = ModifyBookingSerializer(booking, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': #DELETE
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

## CIRCUITS ##

# ALL OF THEM
@api_view(['GET', 'POST'])
def getCircuits(request):

    if request.method == 'GET': #SEE
        circuits = Circuit.objects.all()
        serializer = CircuitSerializer(circuits, many=True) # Many = true for everything, false if only one
        return Response(serializer.data)
    
    elif request.method == 'POST': #CREATE
        serializer = CircuitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# DETERMINED BY ID       
@api_view(['GET'])        
def getCircuitDetail(request, id):
    
    try:
        circuit = Circuit.objects.get(pk=id)
    except Circuit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': #SEE
        serializer = CircuitSerializer(circuit)
        return Response(serializer.data)
    
## CATEGORIES ##

# ALL OF THEM
@api_view(['GET', 'POST'])
def getCategories(request):
    
    if request.method == 'GET': #SEE
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True) # Many = true for everything, false if only one
        return Response(serializer.data)
    
    elif request.method == 'POST': #CREATE
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# DETERMINED BY ID
@api_view(['GET', 'PUT', 'DELETE'])        
def getCategoryDetail(request, id):
    
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': #SEE
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    elif request.method == 'PUT': #UPDATE
        serializer = CategorySerializer(category, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': #DELETE
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
## KARTS ##

# ALL OF THEM
@api_view(['GET'])
def getKarts(request):

    if request.method == 'GET': #SEE
        karts = Kart.objects.all()
        serializer = KartSerializer(karts, many=True) # Many = true for everything, false if only one
        return Response(serializer.data)
    
    elif request.method == 'POST': #CREATE
        serializer = KartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# # Get an event by the specified id
# @api_view(['GET'])
# def getEvent(request, pk):
#     event = Event.objects.get(id=pk)
#     serializer = EventSerializer(event, many=False) # Single object
#     return Response(serializer.data)

# # Create an event
# @api_view(['POST'])
# def createEvent(request):
#     data = request.data
    
#     event = Event.objects.create(
#         body=data['body']
#     )
    
#     serializer = EventSerializer(event, many=False)
#     return Response(serializer.data)

# # Update an event
# @api_view(['PUT'])
# def updateEvent(request, pk):
#     data = request.data
    
#     event = Event.objects.get(id=pk)
#     serializer = EventSerializer(event, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)

# # Delete an event
# @api_view(['DELETE'])
# def deleteEvent(request, pk):
#     event = Event.objects.get(id=pk)
#     event.delete()
#     return Response('Event deleted')