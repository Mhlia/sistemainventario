from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Products, Pedido, Equipo
from .forms import ProductForm, OrderForm, EquipmentForm
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
from openpyxl import Workbook
from .excel_export import generar_excel  # Importar la función para generar el archivo Excel

# Create your views here.

@login_required(login_url='user-login') 
def index(request): # Vista principal del dashboard
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
    # Contexto para la plantilla del dashboard
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
def staff(request): # Vista para gestionar el personal del dashboard
    members = User.objects.all() # Obtener todos los usuarios de la base de datos usando ORM
    members_count = members.count() # Contar el número de usuarios
    orders_count = Pedido.objects.all().count() 
    products_count = Products.objects.all().count() # Contar el número de productos
    
    # Contexto para la plantilla del personal
    context = { 
        'members': members,
        'members_count': members_count,
        'orders_count': orders_count,
        'products_count': products_count,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required(login_url='user-login')
def staff_detail(request, pk): # Vista para mostrar los detalles de un miembro del personal
    members = User.objects.get(id=pk) # Obtener un usuario de la base de datos usando ORM
    context = {
        'members': members,
    }

    return render(request, 'dashboard/staff_detail.html', context)

@login_required(login_url='user-login')
def product(request): # Vista para gestionar los productos del dashboard
    items = Products.objects.all() # Obtener todos los productos de la base de datos usando ORM
    #items = Products.objects.raw(''SELECT * FROM dashboard_products') # Obtener todos los productos de la base de datos usando raw SQL
    products_count = items.count()
    members_count = User.objects.all().count()
    orders_count = Pedido.objects.all().count()

    equipo_por_producto = {} 
    for producto in items: 
        equipo_por_producto[producto.id] = producto.equipo_set.count() # Obtener el número de equipos asociados a cada producto
    # Crear un formulario para agregar productos y equipos

    form = ProductForm()
    equipment_form = EquipmentForm() 

    if request.method == 'POST':
        if 'agregar_producto' in request.POST:
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Producto agregado exitosamente.')
                return redirect('dashboard-product')
    if 'agregar_serial' in request.POST:
        equipment_form = EquipmentForm(request.POST)
        if equipment_form.is_valid():
            equipment_form.save()
            messages.success(request, 'Equipo agregado exitosamente.')
            return redirect('dashboard-product')
        
    # Contexto para la plantilla de productos
    context = { 
        'items': items,
        'form': form,
        'equipment_form': equipment_form,
        'members_count': members_count,
        'products_count': products_count,
        'orders_count': orders_count,
        'equipo_por_producto': equipo_por_producto,
    }
    return render(request, 'dashboard/product.html', context)

@login_required(login_url='user-login')
def product_delete(request, pk): # Vista para eliminar un producto del dashboard
    item = Products.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

def serial_delete(request, pk): # Vista para eliminar un serial de un equipo
    equipo = get_object_or_404(Equipo, id=pk)
    equipo.delete()
    messages.success(request, 'Serial eliminado exitosamente.')
    return redirect('dashboard-product')

def serial_update(request, pk): # Vista para actualizar el serial de un equipo
    equipo = get_object_or_404(Equipo, id=pk)
    if request.method == 'POST':
        nuevo_serial = request.POST.get('serial')
        equipo.serial = nuevo_serial
        equipo.save()
        messages.success(request, 'Serial actualizado exitosamente.')
        return redirect('dashboard-product')


@login_required(login_url='user-login')
def product_update(request, pk): # Vista para actualizar un producto del dashboard
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
def generar_excel_view(request):
    productos = Products.objects.all() 
    wb = generar_excel(productos)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=productos.xlsx'
    wb.save(response)
    return response



@login_required(login_url='user-login')
def orders(request): # Vista para gestionar los pedidos del dashboard
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

