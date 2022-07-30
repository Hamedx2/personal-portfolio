from django.shortcuts import render ,get_object_or_404
from .models import project
def home(request):
    projects = project.objects.order_by('-date')[:3]
    return render(request, 'portfolio.html', { 'projects' : projects })

def detail(request,project_id):
    proj = get_object_or_404(project, pk=project_id)
    return render(request, 'detailp.html',{ 'project':proj })
