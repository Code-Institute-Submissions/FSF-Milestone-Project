from django.shortcuts import render, get_object_or_404, redirect, reverse
from items.models import Item


def view_cart(request):
    return render(request, 'cart/cart_contents.html')


# Code adapted from the Django tutorials in the course
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)  # only exists to ensure item exists.
    quantity = int(request.POST.get('quantity'))
    redirect_URL = request.POST.get('redirect')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity  # I should probably implement messages here during the final stage, to allow for a more dynamic site. I need to for the JS inclusion anyway.
    # Same with the drop-downs on the menu n stuff, actually.

    request.session['cart'] = cart

    return redirect(redirect_URL)


# code adapted from django tutorials, altered by me.
def adjust_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart')

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    cart = request.session.get('cart')

    cart.pop(item_id)

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))
