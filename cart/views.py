from django.shortcuts import render, get_object_or_404, redirect
from items.models import Item


def view_cart(request):
    render(request, 'cart/cart_contents.html')

# Code adapted from the Django tutorials in the course
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_URL = request.POST.get('redirect')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):  # wouldn't having this be the second condition work better? the item not being in the card is generally more common, after all.
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity  # I should probably implement messages here during the final stage, to allow for a more dynamic site. I need to for the JS inclusion anyway.
    # Same with the drop-downs on the menu n stuff, actually.

    request.session['bag'] = bag

    return redirect(redirect_URL)
