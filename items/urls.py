from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('item/', views.item_page, name='item')
]