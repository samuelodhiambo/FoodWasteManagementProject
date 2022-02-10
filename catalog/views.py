from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('home')
        form = FoodForm(request.POST)
        return render(request, template, {'form': form})
    form = FoodForm()
    return render(request, template, {'form': form})

@login_required
def view_items(request, template='viewOrderItem.html'):
    orders = Order.objects.filter(user=request.user.id)
    products = Food.objects.all()
    context = {
        'orders': orders,
        'products': products
    }
    return render(request, template, context)

def order(request, template='viewOrderItem.html'):
    orders = Order.objects.filter(user=request.user.id)
    order = Order()
    if request.method == 'POST':
        pk = request.POST.get('pk')
        print("=====", pk)
        if not Order.objects.filter(user=request.user, product=pk).exists():
            print("=======", 'ian') 
            food = Food.objects.get(id=pk)
            order.user = request.user
            order.product = food
            print("=================", order)
            try:
                order.save()
                return redirect('view')
            except Exception as e:
                error = e + 'Order Failed!!!'
                print(error)
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

def deleteOrder(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        if order.user == request.user:
            order.delete()
            return redirect('view')
        return redirect('view')
    return redirect('view')

@login_required
def my_products(request, template='viewOrderItem.html'):
    my_products = True
    products = Food.objects.filter(user=request.user.id)
    context = {
        'my_products': my_products,
        'products': products
    }
    return render(request, template, context)

def deleteProduct(request, id):
    product = get_object_or_404(Food, id=id)
    if request.method == 'POST':
        if product.user == request.user:
            product.delete()
            return redirect('my_products')
        return redirect('my_products')
    return redirect('my_products')
