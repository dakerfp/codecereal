from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import Post

def posts(request):
    posts = Post.objects.all()

    ctx = {'posts': posts}
    return render_to_response('blog/posts.html', ctx,
                              RequestContext(request))

def post(request, slug):
    post = get_object_or_404(Post,slug=slug)

    ctx = {'post': post}
    return render_to_response('blog/post.html', ctx,
                              RequestContext(request))
