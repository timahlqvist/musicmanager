from django.contrib import admin
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^recordcollection/', include('recordcollection.urls')),
    url(r'^mixtapemanager/', include('mixtapemanager.urls')),
    url(r'^listrecords/', include('listrecords.urls')),
    url(r'^$', views.index, name='index'),
]
