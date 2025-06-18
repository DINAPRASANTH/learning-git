from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

def my_login_view(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('my_login')
        else:
            return render(request,'authpractice/login.html',{'error':'Invalid credentials'})
    return render(request,'authpractice/login.html')