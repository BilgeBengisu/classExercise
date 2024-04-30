from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout


from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy


def home(request):
# If the user is authenticated, redirect to the boards page
    if request.user.is_authenticated:
        return redirect('posts/')
    # Else display the landing page that has link to FAQ, Login, and Registration links
    else:
        return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        login(request)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to the desired URL after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def posts(request):
    return render(request, "posts.html")