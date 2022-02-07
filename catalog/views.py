from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm

# Create your views here.
def home_view(request, template='index.html'):
    return render(request, template)

def add_item(request, template='additem.html'):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
        form = FoodForm(request.POST)
        return render(request, template, {'form': form})
    form = FoodForm()
    return render(request, template, {'form': form})

def view_items(request, template='viewitems.html'):
    products = Food.objects.all()
    context = {
        'products': products,
    }
    return render(request, template, context)