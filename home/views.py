from django.shortcuts import render, redirect, get_object_or_404
from trending.models import Post
from shop.models import (
    Category, SubCategory, Product
)
from .models import HomeVideo

def index(request):
    categories = Category.objects.order_by('-name')
    products = Product.objects.order_by('-sub_category')
    posts = Post.objects.order_by('-created')
    vid = None
    videos = HomeVideo.objects.all()
    if videos:
        vid = HomeVideo.objects.latest('pk')
    return render(request, 'home/index.html', {
        'posts': posts,
        'products': products,
        'categories': categories,
        'vid': vid
    })

