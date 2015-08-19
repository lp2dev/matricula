from django.db import models

# Create your models here.


class Curso(models.Model):

    codigo = models.CharField(max_length=10, null=True, blank=True)
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre
