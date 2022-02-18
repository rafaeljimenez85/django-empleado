from atexit import register
from pyexpat import model
from django.contrib import admin
from .models import Departamento

# Register your models here.

class DepartamentosAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'shor_name',
        'anulate',
    )

admin.site.register(Departamento, DepartamentosAdmin)