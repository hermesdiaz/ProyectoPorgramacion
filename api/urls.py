from django.urls import path
from . import views

urlpatterns = [
	path('empresas/', views.view_empresas, name='home'),
    path('empresas/create/', views.create_view_empresas, name='home'),
    path('empresas/delete/<int:pk>', views.delete_empresas, name='home'),
    path('empresas/actualizar/<int:pk>/', views.update_empresas, name='home2'),
    path('obligaciones/', views.view_obligaciones, name='home'),
    path('obligaciones/create/', views.create_view_obligaciones, name='home'),
    path('obligaciones/delete/<int:pk>', views.delete_obligaciones, name='home'),
    path('obligaciones/actualizar/<int:pk>', views.update_obligaciones, name='home'),
    path('pagos/', views.view_pagos, name='home'),
    path('pagos/create/', views.create_view_pagos, name='home'),
    path('pagos/delete/<int:pk>', views.delete_pagos, name='home'),
    path('pagos/actualizar/<int:pk>', views.update_pagos, name='home'),
]

