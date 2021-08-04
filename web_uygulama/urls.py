
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include(('vaka.urls','vaka'),namespace='vaka')),
    path('admin/', admin.site.urls),
]
