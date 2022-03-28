from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.home,name = 'Home'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, Document_root = settings.MEDIA_ROOT)