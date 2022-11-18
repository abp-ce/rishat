from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import stripe

from .models import Item, Order
from .utils import make_discounts, make_line_items, make_tax_rates
from stripe_test.settings import STRIPE_API_KEY


stripe.api_key = STRIPE_API_KEY

SUCCESS_URL = 'http://localhost:8000/static/success.html'
CANCEL_URL = 'http://localhost:8000/static/cancel.html'


@api_view(['GET'])
def buy_item(request, id):
    order = get_object_or_404(Order, pk=id)
    line_items = make_line_items(order, make_tax_rates(order))
    discounts = make_discounts(order)
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            discounts=discounts,
            mode='payment',
            success_url=SUCCESS_URL,
            cancel_url=CANCEL_URL,
        )
    except Exception as e:
        return Response(str(e))
    return redirect(checkout_session.url)


@api_view(['GET'])
def get_item(request, id):
    item = get_object_or_404(Item, pk=id)
    context = {'item': item}
    return render(request, 'checkout.html', context)


@api_view(['GET'])
def get_order(request, id):
    order = get_object_or_404(Order, pk=id)
    context = {'order': order, 'items': order.order_item.all()}
    return render(request, 'checkout_order.html', context)
