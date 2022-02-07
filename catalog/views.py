from django.shortcuts import render

# Create your views here.
def home_view(request, template='index.html'):
    return render(request, template)

def add_item(request, template='additem.html'):
    return render(request, template)