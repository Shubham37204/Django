from django.contrib import messages
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'welcom {username} ')
            # return redirect('mysite:home') # Redirect to the 'mysite:home' URL
            # Redirect to the login page after successful registration
            return redirect('login')
    else:
        form = CustomUserCreationForm()  # default user creation form by django
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')
