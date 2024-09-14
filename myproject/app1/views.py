from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import UserProfile, UserPreference
from django.contrib.auth import authenticate, login, logout
from .forms import PreferenceForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse 
from inventory.views import product_list

@login_required
def user_dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def select_preferences(request):
    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            print(f"Selected category: {category}")
            # Clear existing preferences for the user
            UserPreference.objects.filter(user=request.user).delete()
            # Save the new preference
            UserPreference.objects.create(user=request.user, category=category)
            return redirect(reverse('product_list'))
        else:
            print(form.errors)  # Print form errors to debug
    else:
        form = PreferenceForm()
    return render(request, 'select_preferences.html', {'form': form})
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
            print("A")
            login(request, user)
            print("B")
            if UserPreference.objects.filter(user=user).exists():
                return redirect('user_dashboard')  # Redirect to product list if preferences exist
            else:
                return redirect('select_preferences')  # Redirect to select preferences if none exist
        else:
            return HttpResponse("Username or Password incorrect!")
    return render(request, 'login.html')

# Logout view
def LogoutPage(request):
    logout(request)
    return redirect('login')
