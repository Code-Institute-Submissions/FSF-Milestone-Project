from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item
from math import trunc
from decimal import Decimal


#  adapted from the django tutorials, once again.
def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        item = get_object_or_404(Item, pk=item_id)
        if item.sale_price:
            total += item_data * item.sale_price
        else:
            total += item_data * item.base_price
        item_count += item_data
        cart_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'item': item,
        })
    delivery_cost = trunc((6+(6*(item_count))**.5)*100)
    delivery_cost = Decimal(delivery_cost)/100
    grand_total = delivery_cost + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
    }
    return context
