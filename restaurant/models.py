from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length = 255);
    no_of_guests = models.PositiveSmallIntegerField();
    booking_date = models.DateTimeField();
    
    def __str__(self) -> str:
        return self.name;
    
class Menu(models.Model):
    title = models.CharField(max_length = 255);
    price = models.DecimalField(max_digits = 10, decimal_places = 2);
    inventory = models.PositiveSmallIntegerField();
    
    def __str__(self) -> str:
        return f"{self.title}, In Stock: {self.inventory}";