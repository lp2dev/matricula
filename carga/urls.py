from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from carga.views import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'matricula.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),

)
