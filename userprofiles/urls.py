from django.urls import path
from . import views


urlpatterns = [
    path('settings', views.account_page, name='profile'),
    path('orders', views.account_orders, name='profile_orders'),
    path('review', views.post_review, name='review'),
]