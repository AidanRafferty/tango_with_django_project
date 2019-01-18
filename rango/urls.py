from django.conf.urls import url
from rango import views

# the remainder of the url is passed into here after rango is stripped by
# the project urls script into here and is mapped to the relevant view 

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #create a mapping to a different view for the remaining url '/about'
    url(r'^about/', views.about, name = 'about'),
]
