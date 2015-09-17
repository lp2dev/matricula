from django.contrib import admin
from carga.models import Curso, Ciclo
# Register your models here.


class CursoAdmin(admin.ModelAdmin):
    list_per_page = 2
    list_display = ("codigo", "nombre", "user")
    search_fields = ("nombre", "codigo",)

admin.site.register(Curso, CursoAdmin)


class CicloAdmin(admin.ModelAdmin):
    list_per_page = 2
    list_display = ("abrev", "descr")
    search_fields = ("abrev", "descr",)

admin.site.register(Ciclo, CicloAdmin)
