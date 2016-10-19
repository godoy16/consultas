# encoding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

SEXO_CHOICE=(('1','Masculino'),
	('2','femenino'),
	)
# Create your models here.
class Medico(models.Model):
	user = models.ForeignKey(User)
	# firstname = models.CharField(max_length=120, help_text='Nombre del medico', verbose_name='Nombre')
	# lastname = models.CharField(max_length=120,help_text='Apellidos',verbose_name = 'Apellidos')
	birthDate = models.DateTimeField(auto_now_add=False)
	identity = models.CharField(max_length = 15,help_text='numero de identidad')
	NoRegister = models.CharField(max_length = 15,help_text='numero de registro de medico')

	def __unicode__(self):
		return self.user.username 

class Paciente(models.Model):
	firstname = models.CharField(max_length=120, help_text='Nombre del paciente', verbose_name='Nombre')
	lastname = models.CharField(max_length=120,help_text='Apellidos',verbose_name = 'Apellidos')
	birthDate = models.DateTimeField(auto_now_add=False)
	identity = models.CharField(max_length = 15,help_text='numero de identidad')
	encargado = models.CharField(max_length = 15,help_text='Encargado del nino',blank=True,null=True)
	sexo = models.CharField(max_length=50,choices=SEXO_CHOICE,null=True,blank=True) 

	def __unicode__(self):
		return self.firstname +'|'+self.lastname

class Direccion(models.Model):
	paciente = models.ForeignKey(Paciente,null=True,blank=True)
	city =  models.CharField(max_length=120, help_text='Nombre del pueblo o ciudad', verbose_name='Pueblo')
	barrio = models.CharField(max_length=120, help_text='Nombre del medico', verbose_name='Barrio',blank=True,null=True)
	ExactlyAddress = models.CharField(max_length=120, help_text='Direccion exacta', verbose_name='Direccion exacta')

	def __unicode__(self):
		return self.city

class Consulta(models.Model):
	medico = models.ForeignKey(Medico)
	paciente = models.ForeignKey(Paciente)
	date = models.DateTimeField(auto_now=True)
	sintomas = models.TextField(help_text='Sintomas del paciente', verbose_name='sintomas')
	diagnostico = models.TextField(help_text='Diagnostico del paciente', verbose_name='Diagnostico')


	def __unicode__(self):
		return self.medico.firstname +'|'+self.paciente.firstname

class Medicamento(models.Model):
	nombre = models.CharField(max_length=100,help_text='nombre del medicamento')
	indicaciones = models.CharField(max_length=100,help_text='indicaciones',blank=True,null=True)
	contraindicaciones = models.CharField(max_length=100,help_text='nombre del medicamento',blank=True,null=True)
	precio = models.IntegerField(help_text='precio del medicamento', null=True,blank=True)


	def __unicode__(self):
		return self.nombre 


class Receta (models.Model):
	medico = models.ForeignKey(Medico)
	paciente = models.ForeignKey(Paciente)
	consulta = models.ForeignKey(Consulta)
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.medico.firstname +'|'+self.paciente.firstname 




class MedicamentoPorReceta(models.Model):
	receta = models.ForeignKey(Receta)
	medicamento = models.ForeignKey(Medicamento,null=True,blank=True)
	medicamento2=models.CharField(max_length=100,null=True,blank=True)
	dosis = models.CharField(max_length=100,null=True,blank=True)
	toma = models.CharField(max_length=100,null=True,blank=True)

	def __unicode__(self):
		return self.medicamento.nombre +'|'+self.dosis


















