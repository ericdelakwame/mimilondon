from django.db import models
from django.urls import reverse
from accounts.models import User


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/%Y/%m/%d', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return '{} ..{}'.format(self.title, str(self.created))

    def get_absolute_url(self):
        return reverse('trending:post_detail', kwargs={'post_pk': self.pk})




class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
