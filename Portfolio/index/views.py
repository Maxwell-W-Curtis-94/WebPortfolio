from django.shortcuts import render
from django.http import HttpResponseRedirect


# from .forms import CategoryForm, BudgetForm
# from .models import Budget, Category

def index(request):
    context = ''
    return render(request=request, template_name='basic_html/index.html', context={'context': context})
