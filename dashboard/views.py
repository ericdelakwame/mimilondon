from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from trending.models import Post
from trending.forms import PostForm
from shop.forms import (
    CategoryForm, SubCategoryForm, ColorForm,
    SizeForm, ProductColorForm, ProductSizeForm
)
from shop.models import (
    SubCategory, Category, Product, Size,
    Color
) 
from django.forms import modelformset_factory
from home.models import HomeVideo
from home.forms import HomeVideoForm
from .forms import NewProductForm
from accounts.models import User

def users(request):
    users = User.objects.all()
    return render(request, 'dashboard/users.html', {
        'users': users
    })


@login_required
def index(request):
    return render(request, 'dashboard/index.html', {

    })


@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('trending:post_detail', post_pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'dashboard/forms/post_form.html', {
        'form': form,
    })


@login_required
def new_subcategory(request, category_pk):
    categories = Category.objects.order_by('-name')
    category = get_object_or_404(Category, pk=category_pk)
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            subcategory = form.save(commit=False)
            subcategory.category = category
            subcategory.save()
            return redirect('dashboard:subcategories', category_pk=category.pk)
    else:
        form = SubCategoryForm()
    return render(request, 'dashboard/forms/subcategory_form.html', {
        'form': form,
        'categories': categories,
        'category': category
    })


@login_required
def new_product(request, subcategory_pk):
    formset = None
    ColorFormSet = modelformset_factory(Color, can_delete=True, fields=('color',), extra=2)
    SizeFormSet = modelformset_factory(Size, can_delete=True, fields=('size',), extra=2)
    subcategory = get_object_or_404(SubCategory, pk=subcategory_pk)
    categories = Category.objects.order_by('-name')
    subcategories = SubCategory.objects.order_by('-name')

    if request.method == 'POST':   
        form = NewProductForm(request.POST, request.FILES)
        color_formset = ColorFormSet(request.POST, request.FILES)
        size_formset = SizeFormSet(request.POST, request.FILES)
        if form.is_valid() and color_formset.is_valid() and size_formset.is_valid():
            product = form.save(commit=False)
            product.sub_category = subcategory
            product = form.save()
            colors = color_formset.save(commit=False)
            sizes = size_formset.save(commit=False)
            product.sub_category = subcategory
            for c in colors:
                c.save()
                product.colors.add(c)

            for s in sizes:
                s.save()
                product.sizes.add(s)          
            return redirect('dashboard:products')
    else:
        form = NewProductForm()
        color_formset = ColorFormSet(queryset=Color.objects.all())
        size_formset = SizeFormSet(queryset=Size.objects.all())
    return render(request, 'dashboard/categories.html', {
        'form': form,
        'subcategory': subcategory,
        'subcategories': subcategories,
        'categories': categories,
        'color_formset': color_formset,
        'size_formset': size_formset,
    })


@login_required
def new_category(request):
    categories = Category.objects.order_by('-name')
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:categories')
    else:
        form = CategoryForm()
    return render(request, 'dashboard/forms/category_form.html', {
        'form': form,
        'categories': categories
    })


def subcategories(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    subcategories = category.subcategories.order_by('-name')
    return render(request, 'dashboard/subcategories.html', {
        'category': category,
        'subcategories': subcategories,
    })


def categories(request):
    categories = Category.objects.order_by('-name')
    subcategories = SubCategory.objects.order_by('-name')
    return render(request, 'dashboard/categories.html', {
        'categories': categories,
        'subcategories': subcategories
    })


def products(request):
    products = Product.objects.order_by('-created')
    return render(request, 'dashboard/products.html', {
        'products': products
    })


def remove_subcategory(request, subcategory_pk):
    subcategory = get_object_or_404(SubCategory, pk=subcategory_pk)
    category = subcategory.category
    subcategory.delete()
    category.save()
    return redirect('dashboard:subcategories', category_pk=category.pk)


def remove_category(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    category.delete()
    return redirect('dashboard:categories', category_pk=category.pk)


def remove_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    product.delete()
    return redirect('dashboard:products')


def edit_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('dashboard:products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'dashboard/forms/edit_product_form.html', {
        'form': form,
        'product': product,
    })

def new_home_video(request):
    if request.method == 'POST':
        form = HomeVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            return redirect('dashboard:home_video_detail', video_pk=video.pk)
    else:
        form = HomeVideoForm()
    return render(request, 'dashboard/forms/home_video_form.html', {
        'form': form
    })


def home_video_detail(request, video_pk):
    video = get_object_or_404(HomeVideo, pk=video_pk)
    return render(request, 'dashboard/home_video_detail.html', {
        'video': video
    })

def edit_home_video(request, video_pk):
    video = get_object_or_404(HomeVideo, pk=video_pk)
    if request.method == 'POST':
        form = HomeVideoForm(request.POST, request.FILES, instance='video')
        if form.is_valid():
            video = form.save()
            return redirect('dashboard:home_video_detail', video_pk=video.pk)
    else:
        form = HomeVideoForm(instance=video)
    return render(request, 'dashboard/forms/edit_home_video_form.html', {
        'form': form
    })


def remove_home_video(request, video_pk):
    video = get_object_or_404(HomeVideo, pk=video_pk)
    video.delete()
    return redirect('dashboard:index')


def add_color(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if request.method == 'POST':
        form = ProductColorForm(request.POST, request.FILES)
        if form.is_valid():
            color, created = Color.objects.get_or_create(color=form.cleaned_data['color'])
            product.colors.add(color)
            return redirect('dashboard:products')
    else:
        form = ProductColorForm()
    return render(request, 'dashboard/forms/color_form.html', {
        'form': form,
        'product': product,
    })


def add_size(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    if request.method == 'POST':
        form = ProductSizeForm(request.POST, request.FILES)
        if form.is_valid():
            size, created = Size.objects.get_or_create(size=form.cleaned_data['size'])
            product.sizes.add(size)
            return redirect('dashboard:products')
    else:
        form = ProductSizeForm()
    return render(request, 'dashboard/forms/size_form.html', {
        'form': form,
        'product': product,
    })
