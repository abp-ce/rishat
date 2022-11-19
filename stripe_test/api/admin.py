from django.contrib import admin

from .models import Coupon, Currency, Item, ItemCurrency, Order, OrderItem, Tax


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class ItemCurrencyInline(admin.TabularInline):
    model = ItemCurrency
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ('items',)
    inlines = [OrderItemInline]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    filter_horizontal = ('currency_options',)
    inlines = [ItemCurrencyInline]


admin.site.register(ItemCurrency)
admin.site.register(OrderItem)
admin.site.register(Tax)
admin.site.register(Coupon)
admin.site.register(Currency)
