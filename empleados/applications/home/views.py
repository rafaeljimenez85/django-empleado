from django.shortcuts import render
from .models import Prueba
from .forms import PruebaForm

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'


class PruebaListView(ListView):
     template_name = "home/lista.html"
     context_object_name = 'listaNumeros'
     queryset = ['0','10','20','30']
   

class ListarPrueba(ListView):
    model = Prueba
    template_name = "home/lista_prueba.html"
    context_object_name = 'lista'



class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    success_url = '/'

