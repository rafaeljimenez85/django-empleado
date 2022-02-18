# Generated by Django 4.0.1 on 2022-02-01 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0002_alter_departamento_name_alter_departamento_shor_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='apellido')),
                ('job', models.CharField(choices=[('0', 'Contador'), ('1', 'Administrador'), ('2', 'Economista'), ('3', 'Analista'), ('4', 'Otro')], max_length=1, verbose_name='Trabajo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
        ),
    ]
