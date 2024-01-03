from django.shortcuts import render
from rest_framework import generics, viewsets, permissions;
from .models import Menu, Booking;
from .serializers import MenuSerializer, BookingSerializer;

# Create your views here.
def index(request):
    return render(request, "index.html", {});

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all();
    serializer_class = MenuSerializer;

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all();
    serializer_class = MenuSerializer;
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all();
    serializer_class = BookingSerializer;
    permission_classes = [permissions.IsAuthenticated];