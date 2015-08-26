from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'matricula.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),



    url(r'^carga/', include('carga.urls')),
)
