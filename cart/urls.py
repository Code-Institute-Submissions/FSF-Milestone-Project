from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
]
