from django.shortcuts import render ,get_object_or_404
from .models import post
def blog(request):
    posts = post.objects.order_by("-date")[:5]
    return render(request,'blog.html',{ 'posts' : posts })

def detail(request,post_id):
    blog = get_object_or_404(post, pk=post_id)
    return render(request, 'detail.html',{'post':blog})
