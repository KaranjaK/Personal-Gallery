from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.CharField(primary_key=True,max_length=20)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_category():
        category = Category.objects.all()
        return category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Location(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def get_locations():
        locations = Location.objects.all()
        return locations

    def save_location(self):
        self.save()

    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name=value)

    def delete_location(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def filter_by_location(location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

    def filter_by_category(category):
        image_category = Image.objects.filter(category__name=category).all()
        return image_category

    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    def search_image(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['date']