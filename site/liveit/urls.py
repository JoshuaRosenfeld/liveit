from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('app.urls')),
    url(r'^', 'app.views.index')
)
