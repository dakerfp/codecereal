from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Post

def posts(request):
    posts = Post.objects.all()

    ctx = {'posts': posts}
    return render_to_response('blog/posts.html', ctx,
                              RequestContext(request))

def post(request, post_id):
    post = Post.objects.get(id=post_id)

    print "XXX"

    ctx = {'post': post}
    return render_to_response('blog/post.html', ctx,
                              RequestContext(request))
