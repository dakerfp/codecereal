from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import core.views as core

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', core.home, name='home'),
    url(r'^about$', core.about, name='about'),
    url(r'^contact$', core.contact, name='contact'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
