from django.shortcuts import render, get_object_or_404, redirect
from items.models import Item


def view_cart(request):
    return render(request, 'cart/cart_contents.html')


# Code adapted from the Django tutorials in the course
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)  # only exists to ensure item exists.
    quantity = int(request.POST.get('quantity'))
    redirect_URL = request.POST.get('redirect')
    print(redirect_URL)
    print(item)
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += 1
    else:
        cart[item_id] = 1  # I should probably implement messages here during the final stage, to allow for a more dynamic site. I need to for the JS inclusion anyway.
    # Same with the drop-downs on the menu n stuff, actually.

    request.session['cart'] = cart
    print(cart)

    return redirect(redirect_URL)
