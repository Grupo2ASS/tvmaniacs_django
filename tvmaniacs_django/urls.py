from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'tvmaniacs.views.home', name='home'),
    url(r'^actors$', 'tvmaniacs.views.actors', name='actors'),
    url(r'^series$', 'tvmaniacs.views.series', name='series'),
    url(r'^actor/(?P<id>\w+)/$', 'tvmaniacs.views.actor_details', name='actor_details'),

    # Examples:
    # url(r'^$', 'tvmaniacs_django.views.home', name='home'),
    # url(r'^tvmaniacs_django/', include('tvmaniacs_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
