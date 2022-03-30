from unicodedata import category
from django.shortcuts import render

from .models import Image, Location, Category
from django.db.models import Q
from django.views.generic.list import ListView

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

# Search 
def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        results = Image.objects.filter(Q(category__name__icontains=searched) | Q(location__name__icontains=searched))
        return render(request, 'personal/search_results.html', {'searched':searched, 'search':results})
    else:
        message = "The category you provided did not march any Categories we have!!"
        return render(request, 'personal/search_results.html', {"message": message})