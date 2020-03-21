from django.db import models
from django.contrib.gis.db.models import PointField
from shop.models import Product, Options
from accounts.models import  Customer
import datetime
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField



class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    tel_no = PhoneNumberField(blank=True)
    country = models.CharField(max_length=50, default='Ghana')
    preferred_delivery_date = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    # point = PointField(null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, related_name='order_items', on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    options = models.ForeignKey(Options, related_name='orders', null=True, on_delete=models.CASCADE)


  

    def __str__(self):
        if self.customer is not None:
            return '{} {}, Order No: {}'.format(self.customer.first_name, self.customer.last_name)
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        if not self.pk:
            self.product.stock -= self.quantity
            self.product.save()
        super(OrderItem, self).save(*args, **kwargs)
