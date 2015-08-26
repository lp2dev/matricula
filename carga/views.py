from django.shortcuts import render
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Ciclo


class CicloSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ciclo
        #fields = ('url', 'abrev', 'desc')


class CicloViewSet(viewsets.ModelViewSet):  # API REST
    queryset = Ciclo.objects.filter()
    serializer_class = CicloSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):  # API REST
    queryset = User.objects.all()
    serializer_class = UserSerializer
