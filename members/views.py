
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def members(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
def home(request):
  template = loader.get_template('home1.html')
  return HttpResponse(template.render())
def product(request):
  template = loader.get_template('product.html')
  return HttpResponse(template.render())

# def home(request):
#    return render(request, "home1.html")

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())
from django.shortcuts import render, redirect





def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page if login is successful

        # If login is unsuccessful, show an error message
        error_message = 'Invalid username or password.'
        return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')




def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return redirect('signup')

        # Create a new user account
        user = User.objects.create_user(username=username, password=password)

        # You can customize this logic further based on your requirements
        # For example, you might want to send a verification email, require additional fields, etc.

        messages.success(request, 'Account created successfully. Please login.')
        return redirect('login')

    return render(request, 'signup.html')



# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.contrib.auth.hashers import make_password

User = get_user_model()

def password_update(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('new_password')

        # Check if the provided username (email) exists in the database
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User with this username does not exist.')
            return redirect('password_update')

        # Update the user's password with the provided new password (you may want to add some password validation here)
        user.password = make_password(password)
        user.save()

        # Optionally, you can log in the user automatically after password update
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

        messages.success(request, 'Password updated successfully.')

        return redirect('login')  # Redirect to the login page after password update

    return render(request, 'password_update.html')
