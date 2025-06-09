from django.shortcuts import render

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



