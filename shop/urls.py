from django.conf.urls import url
from .views import (
    product_list, categories, product_detail,
    ProductSearchView, category_detail, subcategory_detail
) 

app_name = 'shop'


urlpatterns = [
    url(r'^search/products/$', ProductSearchView.as_view(), name='product_search'),
    url(r'^category/(?P<category_pk>\d+)/$', category_detail, name='category_detail'),
    url(r'^subcategory/(?P<subcategory_pk>\d+)/$', subcategory_detail, name='subcategory_detail'),
    url(r'^categories/$', categories, name='categories'),
    url(r'^product/(?P<product_id>\d+)/$', product_detail, name='product_detail'),
    url(r'^products/$', product_list, name='product_list'),
]
