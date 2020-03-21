from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, SubCategory, Product, Color, Size, Options
from .forms import (
    CategoryForm, SubCategory, ProductForm, ColorForm,
    SizeForm, ProductColorForm, ProductSizeForm, OptionsForm
)
from cart.forms import CartAddProductForm
from django.views.generic import ListView
from functools import reduce
from django.db.models import Q
import operator


class ProductSearchView(ListView):
    template_name = 'shop/product_search.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super(ProdoductSearchView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            result = query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list))
            )
        return result


def product_list(request, category_slug=None):
    category = None
    subcategories = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        subcategories = category.subcategories.all()
        products = Product.objects.filter(category=category)

    return render(request, 'shop/products.html', {
        'category': category,
        'categories': categories,
        'subcategories': subcategories,
        'products': products,

    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)   
    subcategory = product.sub_category
    cart_product_form = CartAddProductForm(product)
    related_products = Product.objects.exclude(pk=product.pk).filter(sub_category=subcategory)
    return render(request, 'shop/product_detail.html',

            {
                'product': product,
                'related_products': related_products,
                'cart_product_form': cart_product_form,
                'subcategory': subcategory,
                                            
            })





def categories(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-created')
    return render(request, 'shop/categories.html', {
        'categories': categories,
        'products': products,
    })


def category_detail(request, category_pk):
    categories = Category.objects.order_by('-name')
    category = get_object_or_404(Category, pk=category_pk)
    products = Product.objects.order_by('-created') 
    return render(request, 'shop/categories.html', {
        'category': category,
        'categories': categories,
        'products': products
        
    })


def subcategory_detail(request, subcategory_pk):
    subcategory = get_object_or_404(SubCategory, pk=subcategory_pk)
    category = subcategory.category
    categories = Category.objects.order_by('-name')
    products = Product.objects.order_by('-created')
    return render(request, 'shop/categories.html', {
        'subcategory': subcategory,
        'category': category,
        'categories': categories,
        'products': products,

    })


def category_info(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    return render(request, 'shop/category_detail.html', {
        'category': category
    })