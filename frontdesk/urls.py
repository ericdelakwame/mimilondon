from django.conf.urls import url
from .views import (
    index, categories, subcategories, products,
    new_product
    
)


app_name = 'frontdesk'


urlpatterns = [
    url(r'^new/product/(?P<subcategory_pk>\d+)/$', new_product, name='new_product'),
    url(r'^categories/$', categories, name='categories'),
    url(r'^subcategories/(?P<category_pk>\d+)/$', subcategories, name='subcategories'),
    url(r'^products/$', products, name='products'),
    url(r'^$', index, name='index'),
]
