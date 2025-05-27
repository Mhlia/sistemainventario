from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Products, Pedido
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders = Pedido.objects.all()
    products = Products.objects.all()
    members_count = User.objects.all().count()
    products_count = products.count()
    orders_count = orders.count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user # Asignar el usuario actual al pedido
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()

    context = {
        'orders': orders,
        'form': form,
        'products': products,
        'members_count': members_count,
        'products_count': products_count,
        'orders_count': orders_count,
        
    }

    return render(request, 'dashboard\index.html', context)

@login_required(login_url='user-login')
def staff(request):
    members = User.objects.all() # Obtener todos los usuarios de la base de datos usando ORM
    members_count = members.count() # Contar el número de usuarios
    orders_count = Pedido.objects.all().count() 
    products_count = Products.objects.all().count() # Contar el número de productos
    context = {
        'members': members,
        'members_count': members_count,
        'orders_count': orders_count,
        'products_count': products_count,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required(login_url='user-login')
def staff_detail(request, pk):
    members = User.objects.get(id=pk) # Obtener un usuario de la base de datos usando ORM
    context = {
        'members': members,
    }

    return render(request, 'dashboard/staff_detail.html', context)

@login_required(login_url='user-login')
def product(request):
    items = Products.objects.all() # Obtener todos los productos de la base de datos usando ORM
    #items = Products.objects.raw(''SELECT * FROM dashboard_products') # Obtener todos los productos de la base de datos usando raw SQL
    products_count = items.count()
    members_count = User.objects.all().count()
    orders_count = Pedido.objects.all().count()
    
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('nombre')
            product_brand = form.cleaned_data.get('marca')
            messages.success(request, f'El producto {product_brand} - {product_name} se ha agregado correctamente.')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form': form,
        'members_count': members_count,
        'products_count': products_count,
        'orders_count': orders_count,
    }
    return render(request, 'dashboard/product.html', context)

@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Products.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required(login_url='user-login')
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
    orders = Pedido.objects.all() # Obtener todos los pedidos de la base de datos usando ORM
    orders_count = orders.count()
    members_count = User.objects.all().count() 
    products_count = Products.objects.all().count() 
    context = {
        'orders': orders,
        'members_count': members_count,
        'orders_count': orders_count,
        'products_count': products_count,
    }
    return render(request, 'dashboard/orders.html', context)