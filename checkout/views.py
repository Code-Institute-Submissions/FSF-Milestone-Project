from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from items.models import Item
from .models import Order, OrderItem
from .forms import OrderForm
from cart.context import cart_contents
from userprofiles.models import UserProfile

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be processed right \
                                now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('cart', {})

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'city': request.POST['city'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.stripe_pid = request.POST.get('client_secret').split('_secret')[0]
            order.save()
            for item_id, item_data in cart.items():
                item = get_object_or_404(Item, pk=item_id)
                order_item = OrderItem(
                    order=order,
                    item=item,
                    quantity=item_data
                )
                order_item.save()
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('success', args=[order.order_no]))

    else:
        if not cart:
            messages.error(request, "There's nothing in your \
                                     cart at the moment")
            return redirect(reverse('search'))

        current_cart = cart_contents(request)
        stripe_total = round(current_cart['grand_total'] * 100)
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )
        profile = get_object_or_404(UserProfile, user=request.user)
        form_data = {
            'email': request.user.email,
            'phone': profile.phone,
            'address_line1': profile.address_line1,
            'address_line2': profile.address_line2,
            'city': profile.city,
            'county': profile.county,
            'postcode': profile.postcode,
            'country': profile.country,
        }
        order_form = OrderForm(form_data)

    template = "checkout/checkout.html"
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)


def success(request, order_no):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_no=order_no)

    messages.success(request, f'Thank you for your purchase, \
                                be sent to {order.email}. \
                                Your order number is:{order.order_no}')
    if 'cart' in request.session:
        del request.session['cart']

    if save_info is True:
        saveprofile = get_object_or_404(UserProfile, user=request.user)
        saveprofile.phone = order.phone
        saveprofile.country = order.country
        saveprofile.city = order.city
        saveprofile.address_line1 = order.address_line1
        saveprofile.address_line2 = order.address_line2
        saveprofile.postcode = order.postcode
        saveprofile.county = order.county
        saveprofile.save()

    context = {
        'order': order
    }
    return render(request, 'checkout/acknowledge.html', context)