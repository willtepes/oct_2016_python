from django.shortcuts import render, redirect
from .models import Product

def index(request):
        context = {
            'products' : Product.objects.all()
        }
        return render(request, 'semi_restful_app/index.html', context)

def new(request):
    return render(request, 'semi_restful_app/new.html')

def create(request):
    if request.method == 'POST':
        Product.objects.add_product(request.POST)
    return redirect('products:new')

def destroy(request, id):
     Product.objects.remove_product(id)
     return redirect('products:index')

def show(request, id):
    context={
        'product': Product.objects.get(id=id),
    }
    print(context)
    return render(request, 'semi_restful_app/show.html', context)

def edit(request, id):
    context = {
        'product': Product.objects.get(id=id),
    }
    return render(request, 'semi_restful_app/edit.html', context)

def update(request, id):
    if request.method == 'POST':
        print(request.POST)
        Product.objects.edit_product(request.POST,id)
    return redirect('products:index')
