from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'tvmaniacs.views.home', name='home'),
    url(r'^actors/$', 'tvmaniacs.views.actors', name='actors'),
    url(r'^series/$', 'tvmaniacs.views.series', name='series'),
    url(r'^actor/(?P<imdb_id>\w+)/$', 'tvmaniacs.views.actor_details', name='actor_details'),
    url(r'^series/(?P<imdb_id>\w+)/((?P<season_number>\d+))/$', 'tvmaniacs.views.episodes', name='episodes'),
    url(r'^series/(?P<imdb_id>\w+)/$', 'tvmaniacs.views.series_details', name='series_details'),

    # Examples:
    # url(r'^$', 'tvmaniacs_django.views.home', name='home'),
    # url(r'^tvmaniacs_django/', include('tvmaniacs_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
