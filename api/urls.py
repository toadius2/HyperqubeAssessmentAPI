from django.urls import path
from .views import homePage
from .views import disk
from .views import memory
from .views import cpu

urlpatterns = [
    path('', homePage, name='home'),
    path('disk', disk, name='disk'),
    path('memory', memory, name='memory'),
    path('cpu', cpu, name='cpu'),
]