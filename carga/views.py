from django.shortcuts import render
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions
from .models import Ciclo, NaturalPerson


class NaturalPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = NaturalPerson
        #fields = ('url', 'abrev', 'desc')


class NaturalPersonViewSet(viewsets.ModelViewSet):  # API REST
    queryset = NaturalPerson.objects.filter()
    serializer_class = NaturalPersonSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CicloSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ciclo
        #fields = ('url', 'abrev', 'desc')


class CicloViewSet(viewsets.ModelViewSet):  # API REST
    queryset = Ciclo.objects.filter()
    serializer_class = CicloSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):  # API REST
    queryset = User.objects.all()
    serializer_class = UserSerializer
