from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Post

def posts(request):
    posts = Post.objects.all()

    ctx = {'posts': posts}
    return render_to_response('blog/posts.html', ctx,
                              RequestContext(request))

def hello(request):
    ctx = {'post': {'title': 'Python with ghmm', 'content': 'Lorem ipsum'}}
    return render_to_response('blog/post_summary.html', ctx,
                              RequestContext(request))
