from django.contrib import admin
from models import *
# Register your models here.
class DireccionAdmin(admin.ModelAdmin):
	list_display = ('id','city','barrio','ExactlyAddress')
	list_display_links = ('id','city','barrio','ExactlyAddress')
	search_fields = ('id','city','barrio')
	ordering = ['-id']

class PacienteAdmin(admin.ModelAdmin):
	list_display = ('id','firstname','lastname','birthDate','identity','encargado')
	list_display_links = ('id','firstname','lastname','birthDate','identity','encargado')
	search_fields = ('id',)
	ordering = ['-id']

class MedicoAdmin(admin.ModelAdmin):
	list_display = ('id','user','birthDate','identity','NoRegister')
	list_display_links = ('id','user','birthDate','identity','NoRegister')
	search_fields = ('id',)
	ordering = ['-id']

class ConsultaAdmin(admin.ModelAdmin):
	list_display = ('id','medico','paciente','date','sintomas','diagnostico')
	list_display_links = ('id','medico','paciente','date','sintomas','diagnostico')
	search_fields = ('id',)
	ordering = ['-id']

class MedicamentoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','indicaciones','contraindicaciones')
	list_display_links = ('id','nombre','indicaciones','contraindicaciones')
	search_fields = ('id',)
	ordering = ['-id']

class RecetaAdmin(admin.ModelAdmin):
	list_display = ('id','medico','paciente','consulta','date')
	list_display_links = ('id','medico','paciente','consulta','date')
	search_fields = ('id',)
	ordering = ['-id']

class MedicamentoPorRecetaAdmin(admin.ModelAdmin):
	list_display = ('id','receta','medicamento','dosis')
	list_display_links = ('id','receta','medicamento','dosis')
	search_fields = ('id',)
	ordering = ['-id']


admin.site.register(Direccion,DireccionAdmin)
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Medico,MedicoAdmin)
admin.site.register(Consulta,ConsultaAdmin)
admin.site.register(Medicamento,MedicamentoAdmin)
admin.site.register(Receta,RecetaAdmin)
admin.site.register(MedicamentoPorReceta,MedicamentoPorRecetaAdmin)