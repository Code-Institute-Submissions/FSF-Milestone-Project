from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/<order_no>', views.success, name='success'),
]