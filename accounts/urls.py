from django.conf.urls import url
from django.contrib.auth.views import (
    login, logout
)
from .views import register, profile


app_name = 'accounts'


urlpatterns = [
    url(r'^register/(?P<utype>[-\w]+)/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^login/$', login, {'template_name': 'accounts/forms/login_form.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'accounts:login'}, name='logout'),
]