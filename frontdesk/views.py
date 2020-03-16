from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from shop.models import Category, SubCategory, Product
from accounts.models import (
    User
)
from shop.forms import ProductForm

@login_required
def index(request):
    users = User.objects.order_by('-last_name')
    products = Product.objects.order_by('-name')
    categories = Category.objects.order_by('-name')
    subcategories = SubCategory.objects.order_by('-name')
    return render(request, 'frontdesk/index.html', {
        'users': users,
        'products': products,
        'categories': categories,
        'subcategories': subcategories
    })



def subcategories(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    subcategories = category.subcategories.order_by('-name')
    return render(request, 'frontdesk/subcategories.html', {
        'category': category,
        'subcategories': subcategories,
    })


def categories(request):
    categories = Category.objects.order_by('-name')
    return render(request, 'frontdesk/categories.html', {
        'categories': categories,
    })


def products(request):
    products = Product.objects.order_by('-created')
    return render(request, 'frontdesk/products.html', {
        'products': products
    })


@login_required
def new_product(request, subcategory_pk):
    subcategory = get_object_or_404(SubCategory, pk=subcategory_pk)
    categories = Category.objects.order_by('-name')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.sub_category = subcategory
            product.save()
            return redirect('frontdesk:categories')
    else:
        form = ProductForm()
    return render(request, 'frontdesk/categories.html', {
        'form': form,
        'subcategory': subcategory,
        'categories': categories
    })
