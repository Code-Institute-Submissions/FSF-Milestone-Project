from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
# Create your views here.

from .forms import OrderForm
from cart.context import cart_contents

import stripe


def checkout(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
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
