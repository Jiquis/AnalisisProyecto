from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import generic
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
    else:
        form = UserRegisterForm()

    context = { 'form' : form}
    return render(request, 'registro.html', context)

class ListAlimentos(generic.View):
    template_name = "list_alimentos.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        "alimentos" : Alimentos.objects.filter()
        }
        return render(request, self.template_name, self.context)
    
class ListMedicinas(generic.View):
    template_name = "list_medicinas.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        "medicinas" : Medicinas.objects.filter()
        }
        return render(request, self.template_name, self.context)
    
class ListJuguetes(generic.View):
    template_name = "list_juguetes.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        "juguetes" : Juguetes.objects.filter()
        }
        return render(request, self.template_name, self.context)
    
class ListUtensilios(generic.View):
    template_name = "list_utensilios.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        "utensilios" : Utensilios.objects.filter()
        }
        return render(request, self.template_name, self.context)

class ListTodos(generic.View):
    template_name = "list_todos.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        "alimentos" : Alimentos.objects.filter(),
        "medicinas" : Medicinas.objects.filter(),
        "juguetes" : Juguetes.objects.filter(),
        "utensilios" : Utensilios.objects.filter()
        }
        return render(request, self.template_name, self.context)