from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  # Import this

# Home page view with login_required decorator
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

# Signup view
def SignUp(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        remember = request.POST.get('remember')
        if password != cpassword:
            return HttpResponse("Password and Confirm Password doesn't match")
        else:
            my_user = User.objects.create_user(uname, email, password)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')

# Login view
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password incorrect!")
    return render(request, 'login.html')

# Logout view
def LogoutPage(request):
    logout(request)
    return redirect('login')
