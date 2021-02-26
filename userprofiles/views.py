from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib import messages

from .models import UserProfile, Review
from items.models import Item
from .forms import UserProfileForm, ReviewForm

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
            if 'avatar-clear' in request.POST:
                if request.POST['avatar-clear']:
                    profile.avatar.delete()
                    profile.save()
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
        reviews = Review.objects.filter(user=request.user)
        reviewed_items = []
        for review in reviews:
            reviewed_items.append(review.item)
        context = {
            'orders': orders,
            'reviewed': reviewed_items,
        }
        return render(request, 'userprofiles/account_orders.html', context)
    except Exception as e:
        messages.error(request, f'|{e}| Error accessing your orders, please contact support.')
        return HttpResponse(content=e, status=400)


def post_review(request, item_ID):
    item = get_object_or_404(Item, pk=item_ID)
    reviews = Review.objects.filter(user=request.user)
    old_review = None
    for review in reviews:
        if review.item == item:
            old_review = review

    if old_review:
        review_form = ReviewForm(instance=old_review)
    else:
        review_form = ReviewForm()

    if request.method == 'POST':
        form_data = {
            'user': request.user,
            'item': item,
            'content': request.POST['content'],
            'score': request.POST['score'],
        }
        review_form = ReviewForm(form_data)
        review_form.save()

    context = {
        'review_form': review_form,
        'item': item,
    }

    return render(request, 'userprofiles/user_review.html', context)
