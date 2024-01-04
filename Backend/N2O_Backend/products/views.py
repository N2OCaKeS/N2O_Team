from django.shortcuts import render

# Create your views here. Контроллеры, вьюхи, функции
def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')