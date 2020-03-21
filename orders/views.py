from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderCreateForm
from .models import Order, OrderItem
from cart.cart import Cart
from .tasks import order_created
from accounts.models import Customer
from shop.models import Product, Options
from django.http import JsonResponse
from shop.forms import OptionsForm



def order_create(request):
    cart = Cart(request)
    order = None
    order_item = None
    product = None
    options = None

    for item in cart:
        product = item['product']
        options = product.options.latest('id')
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()            
            for item in cart:
                order_item = OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price'],
                    options=options
                  
                
                )
               
            cart.clear()            
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html', {
                'cart': cart,
                'form': form,
                'customer': '{} {}'.format(order.first_name, order.last_name),
                'options': options
                
            })
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {
        'cart': cart,
        'form': form,
        'options': options
    })
            
