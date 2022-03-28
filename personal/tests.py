from django.test import TestCase
from .models import Category, Location, Image

# Create your tests here.
# Testing the Category Class and Methods
class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(id='3',name='mtaa')
        self.category.save_category

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))
    
    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(id='1',name='Nairobi')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_update_location(self):
        new_location = 'Mombasa'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='Mombasa')
        self.assertTrue(len(changed_location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)