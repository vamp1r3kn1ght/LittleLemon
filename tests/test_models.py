from django.test import TestCase;
from restaurant.models import Menu;

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice Cream", price = 5.69, inventory = 200);
        itemstr = item.__str__();
        self.assertEqual(itemstr, "Ice Cream : 5.69");