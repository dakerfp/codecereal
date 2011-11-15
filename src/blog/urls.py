from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns('blog/',
    url(r'post', views.hello),
    url(r'', views.posts),
)
