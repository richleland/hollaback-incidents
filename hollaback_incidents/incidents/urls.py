from django.conf.urls.defaults import *

urlpatterns = patterns('incidents.views',
    (r'^report/$', 'incident_form'),
)
