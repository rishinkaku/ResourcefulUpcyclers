from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from website.apps.item.models import Donation

from .forms import DonationForm

@login_required
def index(request):
    if(request.user.profile.isOwner):
        return render(request, 'donations/owner_index.html')
    else:
        return render(request, 'donations/customer_index.html')

def inventory(request):
    if(request.user.is_authenticated):
        if(request.user.profile.isOwner):
            return render(request, 'inventory/owner_index.html')
        else:
            return render(request, 'inventory/customer_index.html')
    else:
        return render(request, 'inventory/customer_index.html')