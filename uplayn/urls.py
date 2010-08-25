from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'uplayn.common.views.home', name="home"),
    url(r'^start-group/$', 'uplayn.common.views.start_group',
        name='start_group'),
    url(r'^location/$', 'uplayn.groupsites.views.location', name="location"),

    (r'^groupadmin/', include('uplayn.groupadmin.urls')),

    # django-registration urls
    (r'^accounts/', include('registration.backends.default.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^story/$', 'direct_to_template', {'template': 'story.html'}, name="story"),
)

if settings.SERVE_STATIC_MEDIA:
    """
    Used to serve static media in development environment. To use this,
    create a local_settings file with the following parameters:

    SERVE_STATIC_MEDIA = True
    MEDIA_URL = '/site_media/'
    """
    from django.views.static import serve
    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('', (r'^%s(?P<path>.*)$' % _media_url, serve,
            {'document_root': settings.MEDIA_ROOT}))
    del(_media_url, serve)
