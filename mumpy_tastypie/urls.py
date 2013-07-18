from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api

api = Api(api_name='v1')

from todo.api.resources import TodoResource
api.register(TodoResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mumpy_tastypie.views.home', name='home'),
    # url(r'^mumpy_tastypie/', include('mumpy_tastypie.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	(r'^api/', include(api.urls)),
 )
