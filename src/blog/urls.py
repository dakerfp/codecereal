from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'posts', name='posts'),
    url(r'^post/(?P<slug>[A-Za-z0-9-]+)$', 'post', name='post'),
)
