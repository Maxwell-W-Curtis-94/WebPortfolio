from django.shortcuts import render


# Create your views here.
def index(request):
    context = ''
    return render(request=request, template_name='project_html/project.html', context={'context': context})
