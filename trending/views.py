from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


def posts(request):
    posts = Post.objects.order_by('-created')
    return render(request, 'trending/blog.html', {
        'posts': posts,
    })

@login_required
def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comments = post.comments.order_by('-created')
    other_posts = Post.objects.exclude(pk=post.pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('trending:post_detail', post_pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'trending/post_detail.html', {
        'form': form,
        'comments': comments,
        'post': post,
        'other_posts': other_posts,
    })