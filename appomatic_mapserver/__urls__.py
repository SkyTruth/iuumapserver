from django.conf.urls import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^map/?$', 'appomatic_mapserver.views.index'),
    (r'^map/proxy/?$', 'appomatic_mapserver.proxy.proxy'),
    (r'^map/(?P<application>\w*)/?$', 'appomatic_mapserver.views.application'),
    (r'^map/(?P<application>\w*)/server/?$', 'appomatic_mapserver.views.mapserver'),
)
