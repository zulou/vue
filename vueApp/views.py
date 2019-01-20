from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def  index(request):
    data = {}
    data['home'] = 'active'
    return render(request, 'public/index.html', {'menu': data, })

