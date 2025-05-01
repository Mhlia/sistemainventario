from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Products
from .forms import ProductForm


# Create your views here.
@login_required(login_url='user-login')
def index(request):
    return render(request, 'dashboard\index.html')

@login_required(login_url='user-login')
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required(login_url='user-login')
def product(request):
    items = Products.objects.all() # Obtener todos los productos de la base de datos usando ORM
    #items = Products.objects.raw(''SELECT * FROM dashboard_products') # Obtener todos los productos de la base de datos usando raw SQL
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/product.html', context)

def product_delete(request, pk):
    item = Products.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

def product_update(request, pk):
    item = Products.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required(login_url='user-login')
def orders(request):
    return render(request, 'dashboard/orders.html')