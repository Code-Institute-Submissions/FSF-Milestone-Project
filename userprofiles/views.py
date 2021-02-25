from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from .models import UserProfile
from .forms import UserProfileForm


def account_page(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    profile_form = UserProfileForm(instance=profile)
    if request.method == 'POST':
        form_data = {
            'avatar': request.FILES['avatar'],
            'display_name': request.POST['display_name'],
            'phone': request.POST['phone'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        profile_form = UserProfileForm(form_data)
        if profile_form.is_valid():
            profile.avatar.save(request.FILES['avatar'].name, request.FILES['avatar'])
            profile = profile.save()

    context = {
        'profile': profile,
        'profile_form': profile_form,
    }

    return render(request, "userprofiles/account_page.html", context)


def account_orders(request):
    try:
        profile = get_object_or_404(UserProfile, user=request.user)
        orders = profile.orders.all()
        reviews = profile.reviews.all()

        context = {
            'orders': orders,
            'reviews': reviews,
        }
        return render(request, 'userprofiles/account_orders.html', context)
    except Exception as e:
        messages.error(request, f'|{e}| Error accessing your orders, please contact support.')
        return HttpResponse(content=e, status=400)

def post_review(request):
    return render(request, 'userprofile/user_review.html')