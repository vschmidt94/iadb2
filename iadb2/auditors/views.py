"""
Auditors App - Views module
"""

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    """
    Home view for auditors
    """
    html = "<html><body>It lives</body></html>"
    return HttpResponse(html)
