from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import core.views as core

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', core.home, name='home'),
    url(r'^about$', core.about, name='about'),
    url(r'^contact$', core.contact, name='contact'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve', {'document_root': settings.STATIC_ROOT, 'insecure': True})
)

urlpatterns += staticfiles_urlpatterns()
