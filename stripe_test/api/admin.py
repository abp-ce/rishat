from django.contrib import admin

from .models import Coupon, Item, Order, OrderItem, Tax


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ('items',)
    inlines = [OrderItemInline]


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Tax)
admin.site.register(Coupon)
