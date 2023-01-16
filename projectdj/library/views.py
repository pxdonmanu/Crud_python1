from django.shortcuts import  render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

#I created my first view, it means that this view will be the first that showed when start the app

def start(request):
    return render(request, 'pages/start.html')

def us(request):
    return render(request, 'pages/us.html')

def products(request):
    products= Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def create(request):
    form=ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, 'products/create.html', {'form': form})

def edit(request, id):
    product=Product.objects.get(id=id)
    form=ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('products')
    return render(request, 'products/edit.html', {'form':form})

def delete(request, id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect('products')