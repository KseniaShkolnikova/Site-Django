from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main_view,name='main'),
    path('about/',about_view,name='about'),
    path('cart/',cart_view,name='cart'),
    path('products/',products_view,name='products'),
    
        path('products/electonica',electonica_view,name='electonica'),
    path('products/tehnica',tehnica_view,name='tehnica'),
    path('products/clother',clother_view,name='clother'),
    path('products/for_home',for_home_view,name='for_home'),
    path('products/sport',sport_view,name='sport'),
    path('products/health',health_view,name='health'),
    path('products/children',children_view,name='children'),
    path('products/all',all_view,name='all')
]
