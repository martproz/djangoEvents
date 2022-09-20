from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from events.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
]

handler404 = Error404View.as_view()