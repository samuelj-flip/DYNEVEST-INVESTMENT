from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/pages/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/pages/login.html', {'form': form})

@login_required
def dashboard_view(request):
    # This fetches the specific data for the logged-in user
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/dashboard/index.html', {'profile': profile})

def index_view(request):
    return render(request, 'index.html') # Found in core/templates/

def login_view(request):
        return render(request, 'accounts/pages/login.html') # Found in core/accounts/templates/accounts/pages/


