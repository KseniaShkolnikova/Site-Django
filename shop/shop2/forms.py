from django import forms
from .models import *

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name','description','price','weight','cooking_time','is_spicy',
                  'is_vegetarian','photo','is_available','category']
    
class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['description','photo','name']  

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['cart','menu_item','quantity'] 

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status','total_price','address','comment','payment_method']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order','menu_item','quantity']  