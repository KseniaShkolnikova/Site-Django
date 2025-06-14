from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from basket.forms import *
from django.contrib.auth import login, logout

class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'OrderItem/OrderItem_list.html'
    context_object_name = 'OrderItem'
    
class OrderItemDetailView(DetailView):
    model = OrderItem
    template_name = 'OrderItem/OrderItem_detail.html'
    context_object_name = 'OrderItem'    

class OrderItemCreateView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'OrderItem/OrderItem_form.html'
    success_url= reverse_lazy('OrderItem_list_view')

class OrderItemUpdateView(UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'OrderItem/OrderItem_form.html'
    success_url= reverse_lazy('OrderItem_list_view')    

class OrderItemdeleteView(DeleteView):
    model = OrderItem
    context_object_name = 'OrderItem'    
    template_name = 'OrderItem/OrderItem_confirm_delete.html'
    success_url= reverse_lazy('OrderItem_list_view') 



class OrderListView(ListView):
    model = Order
    template_name = 'Order/Order_list.html'
    context_object_name = 'Order'
    
class OrderDetailView(DetailView):
    model = Order
    template_name = 'Order/Order_detail.html'
    context_object_name = 'Order'    

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'Order/Order_form.html'
    success_url= reverse_lazy('Order_list_view')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'Order/Order_form.html'
    success_url= reverse_lazy('Order_list_view')    

class OrderdeleteView(DeleteView):
    model = Order
    context_object_name = 'Order'    
    template_name = 'Order/Order_confirm_delete.html'
    success_url= reverse_lazy('Order_list_view') 







class CartItemListView(ListView):
    model = CartItem
    template_name = 'CartItem/CartItem_list.html'
    context_object_name = 'CartItem'
    
class CartItemDetailView(DetailView):
    model = CartItem
    template_name = 'CartItem/CartItem_detail.html'
    context_object_name = 'CartItem'    

class CartItemCreateView(CreateView):
    model = CartItem
    form_class = CartItemForm
    template_name = 'CartItem/CartItem_form.html'
    success_url= reverse_lazy('CartItem_list_view')

class CartItemUpdateView(UpdateView):
    model = CartItem
    form_class = CartItemForm
    template_name = 'CartItem/CartItem_form.html'
    success_url= reverse_lazy('CartItem_list_view')    

class CartItemdeleteView(DeleteView):
    model = CartItem
    context_object_name = 'CartItem'    
    template_name = 'CartItem/CartItem_confirm_delete.html'
    success_url= reverse_lazy('CartItem_list_view') 







class CategoriesListView(ListView):
    model = Categories
    template_name = 'Categories/Categories_list.html'
    context_object_name = 'Categories'
    
class CategoriesDetailView(DetailView):
    model = Categories
    template_name = 'Categories/Categories_detail.html'
    context_object_name = 'Categories'    

class CategoriesCreateView(CreateView):
    model = Categories
    form_class = CategoriesForm
    template_name = 'Categories/Categories_form.html'
    success_url= reverse_lazy('Categories_list_view')

class CategoriesUpdateView(UpdateView):
    model = Categories
    form_class = CategoriesForm
    template_name = 'Categories/Categories_form.html'
    success_url= reverse_lazy('Categories_list_view')    

class CategoriesdeleteView(DeleteView):
    model = Categories
    context_object_name = 'Categories'    
    template_name = 'Categories/Categories_confirm_delete.html'
    success_url= reverse_lazy('Categories_list_view') 





class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'MenuItem/MenuItem_list.html'
    context_object_name = 'MenuItem'
    
class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = 'MenuItem/MenuItem_detail.html'
    context_object_name = 'MenuItem'    

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['form_basket'] =BasketAddProductForm()
        return context
        

class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'MenuItem/MenuItem_form.html'
    success_url= reverse_lazy('MenuItem_list_view')

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'MenuItem/MenuItem_form.html'
    success_url= reverse_lazy('MenuItem_list_view')    

class MenuItemdeleteView(DeleteView):
    model = MenuItem
    context_object_name = 'MenuItem'    
    template_name = 'MenuItem/MenuItem_confirm_delete.html'
    success_url= reverse_lazy('MenuItem_list_view') 

# Create your views here.
def main_view (request):
    return render (request, 'main.html')

def about_view (request):
    return render (request, 'about.html')

def cart_view (request):
    return render (request, 'cart.html')

def products_view (request):
    return render (request, 'products.html')

def electonica_view (request):
    return render (request, 'products.html')

def all_view (request):
    return render (request, 'products.html')

def children_view (request):
    return render (request, 'products.html')

def health_view (request):
    return render (request, 'products.html')

def sport_view (request):
    return render (request, 'products.html')

def for_home_view (request):
    return render (request, 'products.html')

def clother_view (request):
    return render (request, 'products.html')

def tehnica_view (request):
    return render (request, 'products.html')

def products_view(request):
    category_id = request.GET.get('category')
    categories = Categories.objects.all()
    
    menu_items = MenuItem.objects.filter(is_available=True)
    current_category = None
    
    if category_id:
        menu_items = menu_items.filter(category_id=category_id)
        current_category = int(category_id)
    
    return render(request, 'products.html', {
        'menu_items': menu_items,
        'categories': categories,
        'current_category': current_category,
    })


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('products')
    else:
        form = LoginForm()
    return render(request,'Auth/Login.html', context={'form':form})  


def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data = request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('products')
    else:
        form = RegistrationForm()
    return render(request,'Auth/Registration.html', context={'form':form}) 

def logout_user(request):
    logout(request)
    return redirect('products')
