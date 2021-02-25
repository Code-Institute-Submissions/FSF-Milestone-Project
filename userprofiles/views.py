from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def account_page(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    profile_form = UserProfileForm(instance=profile)
    if request.method == 'POST':
        if request.FILES:
            form_data = {
                'user': request.user,
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
            profile.avatar.save(request.FILES['avatar'].name, request.FILES['avatar'])
        else:
            if 'avatar' in request.POST:
                if request.POST['avatar']:
                    profile.avatar.delete()
            form_data = {
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
            profile.display_name = form_data['display_name']
            profile.phone = form_data['phone']
            profile.address_line1 = form_data['address_line1']
            profile.address_line2 = form_data['address_line2']
            profile.city = form_data['city']
            profile.county = form_data['county']
            profile.postcode = form_data['postcode']
            profile.country = form_data['country']
            profile.save()
            messages.info(request, "Your profile was successfully updated.")

    context = {
        'avatar': profile.avatar,
        'profile': profile,
        'profile_form': profile_form,
    }

    return render(request, "userprofiles/account_page.html", context)


def account_orders(request):
    try:
        orders = Order.objects.filter(user=request.user)
        context = {
            'orders': orders,
        }
        return render(request, 'userprofiles/account_orders.html', context)
    except Exception as e:
        messages.error(request, f'|{e}| Error accessing your orders, please contact support.')
        return HttpResponse(content=e, status=400)


def post_review(request):
    return render(request, 'userprofile/user_review.html')
