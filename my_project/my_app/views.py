from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.

def home(request):
    return render(request=request, template_name='home.html') 

def items(request):
    products = Item.objects.all()
    return render(
        request=request, 
        template_name='products.html', 
        context={'my_products': products}
    )