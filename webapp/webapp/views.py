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


# login is handled in urls.py


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #using the django user form
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('posts')  # Redirect the user to posts page
    else:
        #if registration failed, prompt the user again
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

#logout
def logout_view(request):
    logout(request)
    return redirect('home') #redirecting the user back to the initial page

@login_required
def posts(request):
    return render(request, "posts.html")