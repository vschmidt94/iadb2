from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """
    Front page for site 
    """
    dict = {'page_heading': 'Internal Audit Dashboard'}
    return render(request, 'dashboard/dashboard.html', dict)
