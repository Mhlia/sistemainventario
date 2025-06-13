from django.urls import path
from . import views

#configuración de las URL del dashboard
urlpatterns = [
    path('dashboard', views.index, name='dashboard-index'), # Página principal del dashboard
    path('staff/', views.staff, name='dashboard-staff'), # Página para gestionar el personal
    path('staff/detail/int<int:pk>/', views.staff_detail, name='dashboard-staff-detail'), # Detalle del personal
    path('product/', views.product, name='dashboard-product'), # Página para gestionar productos
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'), # Eliminar un producto  
    path('product/update/<int:pk>/', views.product_update, name='dashboard-product-update'), # Actualizar un producto
    path('serial/delete/<int:pk>/', views.serial_delete, name='dashboard-serial-delete'), # Eliminar un serial
    path('serial/update/<int:pk>/', views.serial_update, name='dashboard-serial-update'), # Actualizar un serial
    path('orders/', views.orders, name='dashboard-orders'), # Página para gestionar pedidos
    path('product/excel/', views.generar_excel_view, name='dashboard-product-excel')
]