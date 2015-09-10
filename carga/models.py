from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

'''
class MiUser(AbstractUser):

    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = "MiUser"
        verbose_name_plural = "MiUsers"

'''


class NaturalPerson(models.Model):

    last_name = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.TextField(max_length=60)
    birth_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "NaturalPerson"
        verbose_name_plural = "NaturalPersons"

    def __str__(self):
        return self.first_name


class Ciclo(models.Model):

    abrev = models.CharField(max_length=10, null=True, blank=True)
    desc = models.TextField(max_length=60)

    class Meta:
        verbose_name = "Ciclo"
        verbose_name_plural = "Ciclos"

    def __str__(self):
        return self.abrev


class Curso(models.Model):

    codigo = models.CharField(max_length=10, null=True, blank=True)
    nombre = models.CharField(max_length=60)
    user = models.ForeignKey(User, null=True, blank=True)
    ciclo = models.ForeignKey(Ciclo)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre
