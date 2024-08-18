"""iadb2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'IADB2 Database Maintenance'
admin.site.site_title = 'IADB2 Database Maintenance'
admin.site.index_title = 'IADB2 Database Administration'

urlpatterns = [
    path('', include('iadb2.dashboard.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('iadb2.dashboard.urls')),
    path('audits/', include('iadb2.audits.urls')),
    path('auditors/', include('iadb2.auditors.urls')),
    path('events/', include('iadb2.attendance.urls')),
    path('attendance/', include('iadb2.attendance.urls')),
    path('people/', include('iadb2.people.urls')),
    path('processes/', include('iadb2.processes.urls')),
    path('requirements/', include('iadb2.requirements.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)