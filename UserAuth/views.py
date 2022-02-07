from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def signin(request, template='Login.html'):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        error = 'Credentials do not match'
        return render(request, template, {'error': error})
    return render(request, template)

def register(request, template='Register.html'):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, template, {'form': form})
    form = CreateUserForm()
    return render(request, template)

def logout_user(request):
    logout(request)
    return redirect('home')

    