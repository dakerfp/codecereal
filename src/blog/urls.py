from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns('blog/',
    url(r'post/(?P<slug>[A-Za-z0-9-]+)/$', views.post, name='post'),
    url(r'$', views.posts, name='blog'),
)
