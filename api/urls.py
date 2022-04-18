from django.urls import path
from . import views

urlpatterns = [
	path('empresas/', views.view_empresas, name='home'),
    path('empresas/create/', views.create_view_empresas, name='home'),
]

