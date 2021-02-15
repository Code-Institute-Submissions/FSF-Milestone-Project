from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<item_ID>', views.item_page, name='item_page')
]
