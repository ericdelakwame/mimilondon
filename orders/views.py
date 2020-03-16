from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderCreateForm
from .models import Order, OrderItem
from cart.cart import Cart
from .tasks import order_created
from accounts.models import Customer
from shop.models import Size, Product
from django.http import JsonResponse



def order_create(request):
    order = None
    order_item = None
    cart = Cart(request)
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
                    size=product.sizes,
                    color=product.colors
                
                )
               
            cart.clear()            
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html', {
                'cart': cart,
                'form': form,
                'customer': '{} {}'.format(order.first_name, order.last_name)
            })
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {
        'cart': cart,
        'form': form,
    })
            
