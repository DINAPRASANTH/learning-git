from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from django.views.decorators.csrf import csrf_exempt

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'checker/login.html', {'error': 'Invalid credentials'})
    return render(request, 'checker/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'checker/dashboard.html', {'profile': profile})

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'checker/register.html', {'error': 'Username already exists'})
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('complete_profile')
    return render(request, 'checker/register.html')

@login_required
def complete_profile(request):
    if request.method == 'POST':
        UserProfile.objects.create(
            user=request.user,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            clubname=request.POST.get('clubname'),
            position=request.POST.get('position'),
            description=request.POST.get('description')
        )
        return redirect('home')
    return render(request, 'checker/complete_profile.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirect to profile if not created
            if not hasattr(user, 'userprofile'):
                return redirect('complete_profile')
            return redirect('home')
        else:
            return render(request, 'checker/login.html', {'error': 'Invalid credentials'})
    return render(request, 'checker/login.html')

@login_required
def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        profile.clubname = request.POST.get('clubname')
        profile.position = request.POST.get('position')
        profile.description = request.POST.get('description')
        profile.save()
        return redirect('dashboard')
    return render(request, 'checker/edit_profile.html', {'profile': profile})

@login_required
def home(request):
    return render(request, 'checker/dashboard.html') 

#Added this line to see the remote changes on the repo
#learning working of branching
#temporary change