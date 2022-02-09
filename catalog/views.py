from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Food, Order
from .forms import FoodForm

# Create your views here.
def home_view(request, template='index.html'):
    products = Food.objects.all()
    context = {
        'products': products,
    }
    return render(request, template, context)

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

@login_required
def view_items(request, template='viewOrderItem.html'):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, template, context)

def order(request, template='viewOrderItem.html'):
    orders = Order.objects.all()
    order = Order()
    if request.method == 'POST':
        pk = request.POST.get('pk')
        if not Order.objects.get(product=pk): 
            food = Food.objects.get(id=pk)
            order.user = request.user
            order.product = food
            try:
                order.save()
                return redirect('view')
            except Exception as e:
                error = e + 'Order Failed!!!'
                context = {
                    'orders': orders,
                    'error': error
                }
                return render(request, template, context)
        error = 'You have already placed that order'
        context = {
            'orders': orders,
            'error': error
        }
        return render(request, template, context)
    return redirect('home')