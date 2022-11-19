from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view

from .models import Item, Order
from .utils import process_order


@api_view(['GET'])
def buy_order(request, id):
    order = get_object_or_404(Order, pk=id)
    return process_order(order)


@api_view(['GET'])
def buy_item(request, id):
    currency = request.GET['currency']
    item = get_object_or_404(Item, pk=id)
    order = Order.objects.create()
    order.items.add(item)
    return process_order(order, currency)


@api_view(['GET'])
def get_item(request, id):
    item = get_object_or_404(Item, pk=id)
    context = {'item': item, 'currencies': item.currency_options.all()}
    return render(request, 'checkout.html', context)


@api_view(['GET'])
def get_order(request, id):
    order = get_object_or_404(Order, pk=id)
    context = {'order': order, 'items': order.order_item.all()}
    return render(request, 'checkout_order.html', context)
