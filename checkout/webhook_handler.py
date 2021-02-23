from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Order, OrderItem
from items.models import Item

import time


class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200
            )

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        total = round(intent.charges.data[0].amount/100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False

        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    phone__iexact=shipping_details.phone,
                    email__iexact=billing_details.email,
                    address_line1__iexact=shipping_details.address.line1,
                    address_line2__iexact=shipping_details.address.line2,
                    city__iexact=shipping_details.address.city,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    county__iexact=shipping_details.address.state,
                    stripe_pid__iexact=pid,
                    grand_total=total,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                    content=f'webhook recieved: {event["type"]} Order \
                            already exists in database.',
                    status=200
                )
        else:
            order = None
            try:
                order = Order.objects.create(
                        full_name=shipping_details.name,
                        phone=shipping_details.phone,
                        email=billing_details.email,
                        address_line1=shipping_details.line1,
                        address_line2=shipping_details.line2,
                        city=shipping_details.city,
                        country=shipping_details.country,
                        postcode=shipping_details.postal_code,
                        county=shipping_details.state,
                        stripe_pid=pid,
                    )
                for item_id, item_data in cart.items():
                    item = get_object_or_404(Item, pk=item_id)
                    order_item = OrderItem(
                        order=order,
                        item=item,
                        quantity=item_data
                    )
                    order_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'webhook recieved: {event["type"]} Error: Failed to create order. {e}', status=500)
        return HttpResponse(
            content=f'webhook recieved: {event["type"]} Created Order in webhook',
            status=200
            )

    def handle_payment_intent_failed(self, event):
        return HttpResponse(
            content=f'webhook recieved: {event["type"]}',
            status=200
            )
