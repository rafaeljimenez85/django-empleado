from pickle import TRUE
from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habiliadad', max_length=50)

    class meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleados'
    
    def __str__(self):
            return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):
    JOB_CHOICES = (
        ('0', 'Analista Jr'),
        ('1', 'Analista'),
        ('2', 'Consultor'),
        ('3', 'Consultor Senior'),
        ('4', 'Coordinador'),
    )
    first_name = models.CharField('nombre', max_length=50)
    last_name = models.CharField('apellido', max_length=50)
    full_name = models.CharField(
        'Nombre completo',
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Mis empleados'
        ordering = ('-first_name','last_name')
        unique_together = ('first_name', 'last_name')


    def __str__(self):
            return str(self.id) + '-' + self.first_name + '-' + self.last_name + '-' + self.job + '-' + str(self.departamento)