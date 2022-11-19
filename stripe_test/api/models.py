from django.core.validators import MinValueValidator
from django.db import models


class Currency(models.Model):

    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.code


class Item(models.Model):

    name = models.CharField(max_length=50, unique=True)
    currency = models.ForeignKey(
        Currency,
        related_name='item_rel',
        on_delete=models.CASCADE,
        default=1
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency_options = models.ManyToManyField(
        Currency,
        through='ItemCurrency',
        blank=True
    )

    def __str__(self):
        return self.name


class Tax(models.Model):

    display_name = models.CharField(max_length=50, unique=True)
    inclusive = models.BooleanField(default=False)
    percentage = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.display_name


class Coupon(models.Model):

    percent_off = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.percent_off)


class Order(models.Model):

    items = models.ManyToManyField(Item, through='OrderItem')
    tax_rates = models.ManyToManyField(Tax, related_name='order', blank=True)
    coupons = models.ManyToManyField(Coupon, related_name='order', blank=True)

    def __str__(self):
        return str(self.pk)


class ItemCurrency(models.Model):
    item = models.ForeignKey(
        Item,
        related_name='item_currency',
        on_delete=models.CASCADE
    )
    currency = models.ForeignKey(
        Currency,
        related_name='item_currency',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='order_item',
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        Item,
        related_name='order_item',
        on_delete=models.CASCADE
    )
    amount = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(1),
        ),
        default=1
    )

    def __str__(self):
        return str(self.pk)
