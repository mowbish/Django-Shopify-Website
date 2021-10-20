from django.contrib import admin

from orders.models import Discount, OrderItem, Order


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
