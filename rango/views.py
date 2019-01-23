from django.shortcuts import render

from django.http import HttpResponse

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    # {{ boldmessage }} in the template is classed as a template variable
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client
    # We make use of the shortcut function to make our lives easier
    # Note that the first perameter is the template we wish to use

    # A template context is a python dictionary that maps template variable names
    # with python variables
    # Therefore any instance of the template variable will be replaced by
    # the string value associated with the key in the context dictionary with
    # the same name as the template variable.

    # the render helper function takes as input the user's request, the template
    # filename and the context dictionary. The render() function will takes this
    # data and mash it together with the template to produce a complete HTML page
    # that is returned with a HttpResponse. This response is then returned and
    # dispatched to the user's web browser

    # we only need to specify the path rango/index.html as we have defined the
    # templates diretcory in our settings python script

    return render(request, 'rango/index.html', context = context_dict)

    #return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")


def about(request):

    context_dict1 = {'AR': "This Tutorial has been put together by Aidan Rafferty.", 'MEDIA_URL': '/media/'}

    return render(request, 'rango/about.html', context = context_dict1)

    #return HttpResponse("Rango says here is about the page <br/> <a href='/rango/'>Index</a>")


