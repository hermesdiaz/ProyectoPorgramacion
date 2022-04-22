from django.urls import path
from . import views

urlpatterns = [
	path('empresas/', views.view_empresas, name='home'),
    path('empresas/create/', views.create_view_empresas, name='home'),
    path('empresas/delete/<int:pk>', views.delete_empresas, name='home'),
    path('obligaciones/', views.view_obligaciones, name='home'),
    path('obligaciones/create/', views.create_view_obligaciones, name='home'),
    path('obligaciones/delete/<int:pk>', views.delete_obligaciones, name='home'),
    path('pagos/', views.create_view_pagos, name='home'),
    path('pagos/create/', views.create_view_pagos, name='home'),
    path('pagos/delete/<int:pk>', views.delete_pagos, name='home'),
]

