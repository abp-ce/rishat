import stripe


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


def make_line_items(order, tax_rates):
    line_items = []
    for item in order.order_item.all():
        line_items.append(
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": item.item.name},
                    "unit_amount": int(item.item.price * 100),
                },
                "quantity": item.amount,
                'tax_rates': tax_rates,
            }
        )
    return line_items
