"""
People App URL Configuration

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
from iadb2.people import views

urlpatterns = [
    path('', views.PeopleListView.as_view(), name='people'),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name='person_detail'),
    path('person/<int:pk>/update/', views.PersonUpdate.as_view(), name='person_update'),
    path('departments/', views.DepartmentListView.as_view(), name='departments'),
    path('departments/<int:pk>/update/', views.DepartmentUpdate.as_view(), name='department_update'),

    # Unused mappings - People can be updated via modal in the PeopleListView, but
    # if Rest API is used, we may want to move that to it's own page/interface
    # Likewise, may want a delete person page for rest api use
    #path('person/create/', views.PersonCreate.as_view(), name='person_create'),
    #path('dept/create/', views.DepartmentCreate.as_view(), name='department_create'),
    #path('person/<int:pk>/delete/', views.PersonDelete.as_view(), name='person_delete'),
    #path('dept/<int:pk>/delete/', views.DepartmentDelete.as_view(), name='department_delete'),
    #pa
]
