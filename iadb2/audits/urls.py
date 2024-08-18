"""
Audits App URL Configuration

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

from django.urls import path
from iadb2.audits import views

urlpatterns = [
    # path('', views.AuditListView.as_view(), name='audit_inquiry'),
    # path('<int:pk>/', views.AuditUpdateView.as_view(), name='audit_details'),
    path(
        '',
        views.AuditListView.as_view(),
        name='audits'),
    path(
        'periods/',
        views.AuditPeriodListView.as_view(),
        name='audit_periods'),
    path(
        'schedule/',
        views.AuditScheduleListView.as_view(),
        name='audit_schedule'),
    path(
        'templates/',
        views.AuditTemplateListView.as_view(),
        name='audit_templates'),
    path(
        'templates/<int:pk>/update',
        views.AuditTemplateUpdateView.as_view(),
        name='audit_template_update'),
    path(
        'templates/<int:pk>',
        views.AuditTemplateDetailView.as_view(),
        name='audit_template_detail'),
]
