from dataclasses import fields
from django.forms import ModelForm
from .models import Food, Order

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = '__all__'