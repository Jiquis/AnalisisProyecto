"""
URL configuration for Veterinaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', register, name='registro'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    #########################INVENTARIO ###############################
    #lista
    path('inventario/lista/alimentos', ListAlimentos.as_view(), name="lista_alimentos"),
    path('inventario/lista/medicinas', ListMedicinas.as_view(), name="lista_medicinas"),
    path('inventario/lista/juguetes', ListJuguetes.as_view(), name="lista_juguetes"),
    path('inventario/lista/utensilios', ListUtensilios.as_view(), name="lista_utensilios"),
    path('inventario/lista/todos', ListTodos.as_view(), name="lista_todos"),
    #creacion
    path('inventario/nuevo/alimentos', NewAlimentos.as_view(), name="nuevo_alimentos"),
    path('inventario/nuevo/medicinas', NewMedicinas.as_view(), name="nuevo_medicinas"),
    path('inventario/nuevo/juguetes', NewJuguetes.as_view(), name="nuevo_juguetes"),
    path('inventario/nuevo/utensilios', NewUtensilios.as_view(), name="nuevo_utensilios"),
    #edicion
    
]
