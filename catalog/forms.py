from email.policy import default
from django import forms
from django.forms import ModelForm
from .models import Food, Order

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['product_name', 'country', 'county', 'location', 'quantity', 'price', 'pimage',]