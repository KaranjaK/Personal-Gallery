from django.shortcuts import render

from personal.models import Image, Location, Category

# Create your views here.
def home(request):
    pictures = Image.objects.all()
    locations = Location.get_locations()
    category = Category.get_category()
    return render(request, 'personal/index.html', {'images': pictures[::-1], 'locations': locations, 'category':category})
