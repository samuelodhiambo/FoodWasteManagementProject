from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Food
from .forms import FoodForm

# Create your views here.
def home_view(request, template='index.html'):
    return render(request, template)

@login_required
def add_item(request, template='additem.html'):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            food = Food()
            food.user = request.user
            food.product_name = form.cleaned_data['product_name']
            food.country = form.cleaned_data['country']
            food.county = form.cleaned_data['county']
            food.location = form.cleaned_data['location']
            food.quantity = form.cleaned_data['quantity']
            food.price = form.cleaned_data['price']
            food.pimage = request.FILES.get('pimage')
            food.save()
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