from django.shortcuts import render, redirect, HttpResponseRedirect, resolve_url
from .forms import CreateUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def signin(request, template='Login.html'):
    next = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request, user)
            print(request)
            if request.GET.get('next'):
                redirect_to = str(request.GET.get('next'))
                print(redirect_to)
                url = '/add/'
                return HttpResponseRedirect(next)
            return redirect('home')
        error = 'Credentials do not match'
        return render(request, template, {'error': error})
    return render(request, template, {'next': next})

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

    