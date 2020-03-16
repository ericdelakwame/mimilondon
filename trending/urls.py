from django.conf.urls import url
from .views import posts, post_detail



app_name = 'trending'

urlpatterns = [
    url(r'^posts/$', posts, name='posts'),
    url(r'^post/(?P<post_pk>\d+)/$', post_detail, name='post_detail'),
]