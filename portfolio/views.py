from django.shortcuts import render
from .models import project
def home(request):
    projects = project.objects.order_by('-date')[:5]
    return render(request, 'portfolio.html', { 'projects' : projects })
