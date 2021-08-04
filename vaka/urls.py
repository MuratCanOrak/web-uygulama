from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'web_uygulama'

urlpatterns = [
    path('add/', views.add, name="add"),
    # path('control/<str:code>/', views.control, name="control"),
    path('control/', views.control, name="control"),
    
]
