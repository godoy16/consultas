# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 04:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('sintomas', models.TextField(help_text='Sintomas del paciente', verbose_name='sintomas')),
                ('diagnostico', models.TextField(help_text='Diagnostico del paciente', verbose_name='Diagnostico')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(help_text='Nombre del pueblo o ciudad', max_length=120, verbose_name='Pueblo')),
                ('barrio', models.CharField(blank=True, help_text='Nombre del medico', max_length=120, null=True, verbose_name='Barrio')),
                ('ExactlyAddress', models.CharField(help_text='Direccion exacta', max_length=120, verbose_name='Direccion exacta')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='nombre del medicamento', max_length=100)),
                ('indicaciones', models.CharField(blank=True, help_text='indicaciones', max_length=100, null=True)),
                ('contraindicaciones', models.CharField(blank=True, help_text='nombre del medicamento', max_length=100, null=True)),
                ('precio', models.IntegerField(blank=True, help_text='precio del medicamento', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicamentoPorReceta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamento2', models.CharField(blank=True, max_length=100, null=True)),
                ('dosis', models.CharField(blank=True, max_length=100, null=True)),
                ('toma', models.CharField(blank=True, max_length=100, null=True)),
                ('medicamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultas.Medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthDate', models.DateTimeField()),
                ('identity', models.CharField(help_text='numero de identidad', max_length=15)),
                ('NoRegister', models.CharField(help_text='numero de registro de medico', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(help_text='Nombre del paciente', max_length=120, verbose_name='Nombre')),
                ('lastname', models.CharField(help_text='Apellidos', max_length=120, verbose_name='Apellidos')),
                ('birthDate', models.DateTimeField()),
                ('identity', models.CharField(help_text='numero de identidad', max_length=15)),
                ('encargado', models.CharField(blank=True, help_text='Encargado del nino', max_length=15, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('1', 'Masculino'), ('2', 'femenino')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Consulta')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Paciente')),
            ],
        ),
        migrations.AddField(
            model_name='medicamentoporreceta',
            name='receta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Receta'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultas.Paciente'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Medico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Paciente'),
        ),
    ]
