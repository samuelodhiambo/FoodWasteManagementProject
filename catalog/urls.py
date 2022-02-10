"""FoodWasteManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home_view, add_item, order, view_items, order, deleteOrder, my_products, deleteProduct

urlpatterns = [
    path('', home_view, name='home'),
    path('add/', add_item, name='add_item'),
    path('view/', view_items, name='view'),
    path('order/', order, name='order'),
    path('delete/<id>/', deleteOrder, name='delete'),
    path('my_products', my_products, name='my_products'),
    path('product/<id>/delete', deleteProduct, name='deleteproduct'),
]