from django.test import TestCase;
from restaurant.models import Menu;
from restaurant.serializers import MenuSerializer;

class MenuViewSet(TestCase):
    def setUp(self):
        self.item = Menu.objects.create(title = "test", price = 99.99, inventory = 200);
        
    def test_getall(self):
        serializer = MenuSerializer(self.item);
        self.assertEqual(serializer.data, {
            "id" : 2,
            "title" : "test",
            "price" : 99.99,
            "inventory" : 200
        });