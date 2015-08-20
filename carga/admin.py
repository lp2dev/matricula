from django.contrib import admin
from carga.models import Curso
# Register your models here.


class CursoAdmin(admin.ModelAdmin):
    list_per_page = 2
    list_display = ("codigo", "nombre", "user")
    search_fields = ("nombre", "codigo",)

admin.site.register(Curso, CursoAdmin)
