from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('more', views.more, name='more'),
    path('celulares',views.celulares, name='celulares'),
    path('laptops',views.laptops, name='laptops'),
    path('pcs',views.pcs, name='pcs'),
]
