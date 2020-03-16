from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import Customer


@login_required
def index(request):
    return render(request, 'customer/index.html', {

    })

def customer_detail(request, customer_pk):
    customer = get_object_or_404(Customer, pk=customer_pk)
    return render(request, 'customer/customer_detail.html', {
        'customer': customer
    })