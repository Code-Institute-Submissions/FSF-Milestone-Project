from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from items.models import Item
from .models import Order, OrderItem
from .forms import OrderForm
from cart.context import cart_contents

import stripe


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
            order = order_form.save()
            for item_id, item_data in cart.items():
                item = get_object_or_404(Item, pk=item_id)
                line_item = OrderItem(
                    order=order,
                    item=item,
                    quantity=item_data
                )
                line_item.save()
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('success', args=[order.order_no]))

    else:
        if not cart:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect(reverse('search'))

        current_cart = cart_contents(request)
        stripe_total = round(current_cart['grand_total'] * 100)
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        order_form = OrderForm()
    
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

    context = {
        'order':order
    }
    return render(request, 'checkout/acknowledge.html', context)