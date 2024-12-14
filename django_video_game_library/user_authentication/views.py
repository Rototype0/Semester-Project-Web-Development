from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, UpdateUserForm, UpdatePasswordForm

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('games_list')
            else:
                messages.error(request, ("There was an error logging in, try again."))
                return redirect('game_lib_login')        
        else:
            return render(request, 'authenticate/login.html', {})
    else:
        messages.error(request, ("You are currently logged in"))
        return redirect('games_list')

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        messages.error("User not authenticated")
    return redirect('games_list')

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = UpdatePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ("Password has been updated"))
                return redirect('game_lib_login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                form = UpdatePasswordForm(current_user)
                return render(request, 'authenticate/update_password.html', {'form': form})
        else:
            form = UpdatePasswordForm(current_user)
            return render(request, 'authenticate/update_password.html', {'form': form})
    else:
        messages.error(request, ("User not authenticated"))
        return redirect('games_list')

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, ("User update successful!"))
            return redirect('game_lib_update_user')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
        return render(request, 'authenticate/update_user.html', {'form': form})
    else:
        messages.error(request, ("User not authenticated"))
        return redirect('games_list')


def register_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, ("Registration successful!"))
                return redirect('games_list')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
        else:
            form = RegisterUserForm()

        context = {'form':form,}
        return render(request, 'authenticate/register_user.html', context)
    else:
        messages.error(request, ("You are currently logged in"))
        return redirect('games_list')