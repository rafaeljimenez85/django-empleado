from multiprocessing import context
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from .models import Empleado, Habilidades

#Importacion de formularios forms.py
from .forms import EmpleadoForm


class InicioView(TemplateView):
    """VIsta de la pagina de inicio"""
    template_name='inicio.html'

# 1. - Listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    paginate_by = 5
    ordering = 'first_name'

    def get_queryset(self):
        palabraClave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            #este es el correcto pero los usuarios no tienen full name
            #full_name__icontains=palabraClave
            first_name__icontains=palabraClave
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = "persona/lista_empleados.html"
    paginate_by = 5
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado


# 2. - Listar todos los empleados que pretenecen a un area de la empresa
class EmpleadosByArea(ListView):
    model = Empleado
    template_name = "persona/list_by_area.html"
    context_object_name='empleados'
    #queryset = Empleado.objects.filter(
    #    departamento__name='SOC Supervisor'
    #)
    def get_queryset(self):
        area = self.kwargs['urlname']
        lista = Empleado.objects.filter(
        departamento__name=area
    )
        return lista
    

#3. - Listar empleados por trabajo
# No funciona
class ListEmpleadosByJob(ListView):
    model = Empleado
    template_name = "persona/list_by_job.html"
    def get_queryset(self):
        job = self.kwargs['urljob']
        lista = Empleado.object.filter(
            Empleado__job=job
        )
        return lista
    


#4. - Listar los empleados por palabra clave


class ListEmpleadosByKword(ListView):
    model = Empleado
    template_name = "persona/list_by_kword.html"
    context_object_name = 'empleados'
    def get_queryset(self):
        print ('***************************************')
        palabraClave = self.request.GET.get("kword",'')
        print ('*******************', palabraClave, '********************')
        lista = Empleado.objects.filter(
        first_name=palabraClave
        )
        print ('Lista resultado:', lista)
        return lista
    


#5. - Listar habilidades de un empleado

class ListHabilidadesEmpleado(ListView):
    model = Empleado
    template_name = "persona/habilidades.html"
    context_object_name = 'habilidades'
    def get_queryset(self):
        empleado = Empleado.objects.get(id=3)
        return empleado.habilidades.all()
    



class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['Titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    # fields con campos especificos
    form_class = EmpleadoForm
    #fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'hoja_vida', 'avatar']
    #fields con todos los campos
    #fields = ('__all__')
    #misma pagina
    #success_url= '.'
    #Una pagina que dice que se cargo corretamente:
    #success_url='/success/'
    success_url=reverse_lazy('persona_app:empleados_all')
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields=['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url=reverse_lazy('persona_app:empleados_admin')


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url=reverse_lazy('persona_app:empleados_admin')

