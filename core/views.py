from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import *
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
    
## Crear Alimentos
class NewAlimentos(generic.CreateView):
    template_name = "new_alimento.html"
    model = Alimentos
    form_class = AlimentosForm
    success_url = reverse_lazy("lista_alimentos")
    
class ListMedicinas(generic.View):
    template_name = "list_medicinas.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        "medicinas" : Medicinas.objects.filter()
        }
        return render(request, self.template_name, self.context)

##Crear Medicinas
class NewMedicinas(generic.CreateView):
    template_name = "new_medicinas.html"
    model = Medicinas
    form_class = MedicinasForm
    success_url = reverse_lazy("lista_medicinas")

class ListJuguetes(generic.View):
    template_name = "list_juguetes.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        "juguetes" : Juguetes.objects.filter()
        }
        return render(request, self.template_name, self.context)
    
#Crear Juguetes
class NewJuguetes(generic.CreateView):
    template_name = "new_juguetes.html"
    model = Juguetes
    form_class = JuguetesForm
    success_url = reverse_lazy("lista_juguetes")


class ListUtensilios(generic.View):
    template_name = "list_utensilios.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        "utensilios" : Utensilios.objects.filter()
        }
        return render(request, self.template_name, self.context)
#Crear utensilios
class NewUtensilios(generic.CreateView):
    template_name = "new_utensilios.html"
    model = Utensilios
    form_class = UtensiliosForm
    success_url = reverse_lazy("lista_utensilios")
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
    
##########Modificar elementos
class UpdateAlimentos(generic.UpdateView):
    template_name = "update_alimentos.html"
    model = Alimentos
    form_class = UpdateAlimentosForm
    success_url = reverse_lazy("lista_alimentos")

class UpdateJuguetes(generic.UpdateView):
    template_name = "update_juguetes.html"
    model = Juguetes
    form_class = UpdateJuguetesForm
    success_url = reverse_lazy("lista_juguetes")

class UpdateMedicinas(generic.UpdateView):
    template_name = "update_medicinas.html"
    model = Medicinas
    form_class = UpdateMedicinasForm
    success_url = reverse_lazy("lista_medicinas")


class UpdateUtensilios(generic.UpdateView):
    template_name = "update_utensilios.html"
    model = Utensilios
    form_class = UpdateUtensiliosForm
    success_url = reverse_lazy("lista_utensilios")

##Borrar elementos
class DeleteAlimentos(generic.DeleteView):
    template_name = "delete_alimentos.html"
    model = Alimentos
    success_url = reverse_lazy("lista_alimentos")

class DeleteJuguetes(generic.DeleteView):
    template_name = "delete_juguetes.html"
    model = Juguetes
    success_url = reverse_lazy("lista_juguetes")

class DeleteMedicinas(generic.DeleteView):
    template_name = "delete_medicinas.html"
    model = Medicinas
    success_url = reverse_lazy("lista_medicinas")

class DeleteUtensilios(generic.DeleteView):
    template_name = "delete_utensilios.html"
    model = Utensilios
    success_url = reverse_lazy("lista_utensilios")


##Serializers
    #alimentos
class AlimentosListCreate(generics.ListCreateAPIView):
    queryset = Alimentos.objects.all()
    serializer_class = AlimentoSerializer

class AlimentosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alimentos.objects.all()
    serializer_class = AlimentoSerializer
#medicinas
class MedicinasListCreate(generics.ListCreateAPIView):
    queryset = Medicinas.objects.all()
    serializer_class = MedicinasSerializer

class MedicinasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicinas.objects.all()
    serializer_class = MedicinasSerializer
#juguetes
class JuguetesListCreate(generics.ListCreateAPIView):
    queryset = Juguetes.objects.all()
    serializer_class = JuguetesSerializer

class JuguetesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Juguetes.objects.all()
    serializer_class = JuguetesSerializer
#Utensilios
class UtensiliosListCreate(generics.ListCreateAPIView):
    queryset = Utensilios.objects.all()
    serializer_class = UtensiliosSerializer

class UtensiliosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Utensilios.objects.all()
    serializer_class = UtensiliosSerializer