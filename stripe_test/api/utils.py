from django.shortcuts import redirect
import stripe
from rest_framework.response import Response

from stripe_test.settings import STRIPE_API_KEY


stripe.api_key = STRIPE_API_KEY

SUCCESS_URL = '/static/success.html'
CANCEL_URL = '/static/cancel.html'


def make_tax_rates(order):
    tax_rates = []
    for tax in order.tax_rates.all():
        tax_rate = stripe.TaxRate.create(
            display_name=tax.display_name,
            inclusive=tax.inclusive,
            percentage=tax.percentage,
        )
        tax_rates.append(tax_rate.id)
    return tax_rates


def make_discounts(order):
    discounts = []
    for coup in order.coupons.all():
        coupon = stripe.Coupon.create(percent_off=coup.percent_off)
        discounts.append({'coupon': coupon.id})
    return discounts


def make_currency_options(item):
    currency_options = {}
    for opt in item.item_currency.all():
        u_a = int(opt.price * 100)
        currency_options[opt.currency.code] = {'unit_amount': u_a}
    return currency_options


def make_line_items(order, tax_rates):
    line_items = []
    for item in order.order_item.all():
        currency_options = make_currency_options(item.item)
        price = stripe.Price.create(
                    currency=item.item.currency,
                    product_data={'name': item.item.name},
                    unit_amount=int(item.item.price * 100),
                    currency_options=currency_options
        )
        line_items.append(
            {
                'price': price.id,
                'quantity': item.amount,
                'tax_rates': tax_rates,
            }
        )
    return line_items


def process_order(request, order, currency='rub'):
    line_items = make_line_items(order, make_tax_rates(order))
    discounts = make_discounts(order)
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            discounts=discounts,
            mode='payment',
            success_url=request.build_absolute_uri(SUCCESS_URL),
            cancel_url=request.build_absolute_uri(CANCEL_URL),
            currency=currency
        )
    except Exception as e:
        return Response(str(e))
    return redirect(checkout_session.url)
