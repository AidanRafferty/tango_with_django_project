from django.conf.urls import url
from rango import views

    # The remainder of the url is passed into here after 'rango/' is stripped by
    # the project urls script via the include() function. Once the include()
    # function is executed in the project script this strips the remainder of the
    # url that has matched so far and passes the remainder into
    # this script for further processing.



urlpatterns = [


    # Create a mapping to the index view if the remainder of the url
    # is an empty string after the first part has been stripped by
    # the project urls python script.

    
    url(r'^$', views.index, name='index'),


    # create a mapping to the about view if the reainder of the url is 'about/'

    
    url(r'^about/', views.about, name='about'),
]

