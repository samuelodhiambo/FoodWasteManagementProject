from django.shortcuts import render

# Create your views here.
def login(request, template='Login.html'):
    return render(request, template)

def register(request, template='Register.html'):
    return render(request, template)

    