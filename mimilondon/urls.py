from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^orders/', include('orders.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^trending/', include('trending.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^customer/', include('customer.urls')),
    url(r'^frontdesk/', include('frontdesk.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^', include('home.urls')),
    # url(r'^cart/', include('cart.urls')),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
