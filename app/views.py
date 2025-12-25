from django.shortcuts import render

from app.forms import CommentForm
from app.models import Post

# Create your views here.
def index(request):
    posts=Post.objects.all()
    context={"posts":posts}
    return render(request,'app/index.html',context)
def post_page(request,slug):
    post=Post.objects.get(slug=slug)
    forms=CommentForm()
    if post.view_count is None:
        post.view_count=1
    else:
        post.view_count=post.view_count+1
    post.save()
    context={'post':post, 'forms':forms}
    return render(request,'app/post.html',context)