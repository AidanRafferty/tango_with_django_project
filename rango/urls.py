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


    # create a mapping to the about view if the remainder of the url is 'about/'

    
    url(r'^about/', views.about, name='about'),


    # the regular expression [\w\-]+ will look for any sequence of alphanumeric
    # characters and any hyphens denoted by \-, and we can match any number of these
    # as we like denoted by the []+ expression.

    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),

    # in the above url mapping will therefore match any sequenvce of alphanumeric
    # characters and hyphens which are in between the rango/cataegory/ and the
    # trailing /. This will then be stored in the perameter category_name_slug and
    # passed into views.show_category().

    # For example, the URL rango/category/pythonbooks/ would result in the
    # category_name_slug having the value, python-books.
    # However, if the URL was rango/category/££££-$$$$$/ then the sequence of
    # characters between rango/category/ and the trailing / would not match the
    # regular expression, and a 404 not found error would result as there is no
    # matching URL pattern.

    # All view functions defined as part of a Django applications must take atleast one parameter.
    # This is typically called request - and provides access to information related to the given HTTP
    # request made by the user. When parameterising URLs, you supply additional named parameters
    # to the signature for the given view. That is why our show_category() view was defined as def
    # show_category(request, category_name_slug).
]

