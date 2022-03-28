from django.test import TestCase
from .models import Category, Location, Image

# Create your tests here.
# Testing the Category Class and Methods
class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(name='mtaa')
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