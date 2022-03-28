from django.shortcuts import render

from .models import Image, Location, Category

# Create your views here.

#Landing page View
def home(request):
    pictures = Image.objects.all()
    locations = Location.get_locations()
    categories = Category.get_category()
    return render(request, 'personal/index.html', {'images': pictures[::-1], 'locations': locations, 'category':categories})

#View Images by Location
def image_location(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'personal/location.html', {'location_images': images})

# View images by category
def image_category(request, category):
    images = Image.filter_by_category(category)
    return render(request, 'personal/category.html', {'category_images': images})

