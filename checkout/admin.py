from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('order_item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)
    readonly_fields = ('order_no', 'date', 'delivery_total',
                       'order_total', 'grand_total',
                       'stripe_pid')
    fields = ('order_no', 'full_name', 'email',
              'phone', 'country', 'county', 'city', 'postcode',
              'address_line1', 'address_line2', 'date', 'delivery_total',
              'order_total', 'grand_total', 'stripe_pid')
    list_display = ('order_no', 'date', 'full_name',
                    'order_total', 'delivery_total', 'grand_total',)
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
