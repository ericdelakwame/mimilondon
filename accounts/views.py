from django.shortcuts import (
    render, redirect, get_object_or_404
)

from .models import (
    User, Admin, Customer, Staff
)

from .forms import (
    AdminForm, CustomerForm, StaffForm
)
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .tasks import welcome_email



def profile(request):
    if request.user.is_customer:
        return redirect('customer:index')
    elif request.user.is_superuser:
        return redirect('dashboard:index')
    elif request.user.is_staff :
        return redirect('frontdesk:index')
    else:
        return HttpResponse('<h2> Unknown user. Please contact support</h2>')


def register(request, utype=None):
    new_user = None
    form = None
    if request.method == 'POST':
        if utype == 'customer':
            form = CustomerForm(request.POST, request.FILES)
        elif utype == 'staff':
            form = StaffForm(request.POST, request.FILES)
        elif utype == 'admin':
            form = AdminForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)
            if utype == 'customer':
                new_user.is_customer = True
            elif utype == 'staff':
                new_user.is_staff = True
            elif utype == 'admin':
                new_user.is_admin = True
                new_user.is_superuser = True
                new_user.is_staff = True
            new_user.save()
            welcome_email.delay(new_user.email)
            raw_password = form.cleaned_data['password1']
            username = form.cleaned_data['username']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:profile')
    else:
        if utype == 'customer':
            form = CustomerForm()
        elif utype == 'staff':
            form = StaffForm()
        elif utype == 'admin':
            form = AdminForm()
    return render(request, 'accounts/forms/registration_form.html', {
        'utype': utype,
        'form': form,
    })


