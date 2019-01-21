"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rango import views

# this script strips the host part of the url
# and rango and passes into the application
# url script 
urlpatterns = [
    
    url(r'^$', views.index, name='index'),

    
    # This mapping below looks for URL strings that match the patterns
    # ^rango/. When a match is made the remainder of the URL string
    # (after rango/ has been stripped from it) is then
    # passed onto and handled by rango.urls through the use of the
    # include() function. The application script (rango.urls) will then handle
    # the remainder of the url and match it to the appropriate view. 

    
    url(r'^rango/', include('rango.urls')),
    
    url(r'^admin/', admin.site.urls),
]
