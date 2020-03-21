from django.conf.urls import url
from .views import (
    index, new_post, new_product, new_subcategory, new_category,
    subcategories, categories, products, remove_category,
    remove_subcategory, edit_product, remove_product,
    new_home_video, home_video_detail, edit_home_video,
    remove_home_video, add_color, add_size, users
) 


app_name = 'dashboard'


urlpatterns = [
    url(r'^users/$', users, name='users'),
    url(r'^add/size/(?P<product_pk>\d+)/$', add_size, name='add_size'),
    url(r'^add/color/(?P<product_pk>\d+)/$', add_color, name='add_color'),
    url(r'^remove/home/video(?P<video_pk>\d+)/$', remove_home_video, name='remove_video'),
    url(r'^edit/home/video/(?P<video_pk>\d+)/$', edit_home_video, name='edit_home_video'),
    url(r'^new/home/video/$', new_home_video, name='new_home_video'),
    url(r'^home/video/(?P<video_pk>\d+)/$', home_video_detail, name='home_video_detail'),
    url(r'^remove/product/(?P<product_pk>\d+)/$', remove_product, name='remove_product'),
    url(r'^edit/product/(?P<product_pk>\d+)/$', edit_product, name='edit_product'),
    url(r'^remove/category/$', remove_category, name='remove_category'),
    url(r'^remove/subcategory/(?P<subcategory_pk>\d+)/$', remove_subcategory, name='remove_subcategory'),
    url(r'^categories/$', categories, name='categories'),
    url(r'^products/$', products, name='products'),
    url(r'^subcategories/(?P<category_pk>\d+)/$', subcategories, name='subcategories'),
    url(r'^new/category/$', new_category, name='new_category'),
    url(r'^new/subcategory/(?P<category_pk>\d+)/$', new_subcategory, name='new_subcategory'),
    url(r'^new/product/(?P<subcategory_pk>\d+)/$', new_product, name='new_product'),
    url(r'^new/post/$', new_post, name='new_post'),
    url(r'^$', index, name='index'),
]
