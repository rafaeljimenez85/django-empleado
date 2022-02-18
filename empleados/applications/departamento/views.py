from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications.persona.models import Empleado
from .models import Departamento
from .forms import NewDepartamentoFrom
# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'
    paginate_by = 5


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoFrom
    success_url='/'

    def form_valid(self, form):
        print('Estamos en el Formvalid')

        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']
        )
        depa.save()


        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )
        return super(NewDepartamentoView, self).form_valid(form)
