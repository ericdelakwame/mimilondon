from django.conf.urls import url
from .views import index, customer_detail


app_name = 'customer'


urlpatterns = [
    url(r'^customer/(?P<customer_pk>\d+)/$', customer_detail, name='customer_detail'),
    url(r'^$', index, name='index'),
]
