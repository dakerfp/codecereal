from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns('blog/',
    url(r'post/(?P<post_id>\d+)/', views.post, name='post'),
    url(r'', views.posts, name='blog'),
)
