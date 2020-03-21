from django.shortcuts import (
    render, get_object_or_404, redirect
)

from django.views.decorators.http import require_POST
from shop.models import Product, Options
from .cart import Cart
from .forms import CartAddProductForm
from shop.forms import OptionsForm, SizeForm, ColorForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(product, request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        Options.objects.create(
            product=product,
            size=cd['size'],
            color=cd['color'],
        )
        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update'],
         
        )
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    for i in product.options.all():
        i.delete()
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    product_options = None
    for item in cart:
        product = item['product']
        product_options = product.options.latest('pk')       
        item['update_quantity_form'] = CartAddProductForm(   product,       
            initial={
                'quantity': item['quantity'],
                'update': True,
            
            }

    
        )
    
    return render(request, 'cart/detail.html', {
        'cart': cart,
        'product_options': product_options,
    })
