from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.home,name = 'Home'),
    url(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
    url(r'^category/(?P<category>\w+)/', views.image_category, name='category'),
    url(r'^search/', views.search_results, name='search'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)