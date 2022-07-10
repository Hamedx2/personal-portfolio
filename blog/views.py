from django.shortcuts import render
from .models import post
def blog(request):
    posts = post.objects.order_by("-date")[:5]
    return render(request,'blog.html',{ 'posts' : posts })
