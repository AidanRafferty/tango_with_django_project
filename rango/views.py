from django.shortcuts import render

from django.http import HttpResponse

from rango.models import Category

from rango.models import Page

from rango.forms import CategoryForm

from rango.forms import PageForm


def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    # {{ boldmessage }} in the template is classed as a template variable
    # context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

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
    # templates directory in our settings python script


    # Query the database for a list of all category objects currently stored
    # Order the categories in descending order (using the -) and retrieve
    # the top 5 - or all if < 5 - by using [:5]
    # Place the list in our context dictionary that will be passed to the tenmplate
    # engine
    # Then do the same for the top 5 most viewed pages 
    category_list = Category.objects.order_by('-likes')[:5]

    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {'categories': category_list, 'pages': page_list}
    
    # render the response and send it back
    return render(request, 'rango/index.html', context = context_dict)

    #return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")


def about(request):

    context_dict1 = {'AR': "This Tutorial has been put together by Aidan Rafferty.", 'MEDIA_URL': '/media/'}

    return render(request, 'rango/about.html', context = context_dict1)

    #return HttpResponse("Rango says here is about the page <br/> <a href='/rango/'>Index</a>")

def show_category(request, category_name_slug):

    # category_name_slug is passed in to this view function as a perameter. 

    # category_name_slug is the final part of the url that will be mapped to this view. 
    # the url will be of the form -  /rango/category/<categoryname-slug>/
    # eg rango/category/python/ will be for the python pages and
    # rango/category/other-frameworks will lead to a view showing the pages of the
    # Other Frameworks Category.

    # Create a template context dictionary that will be passed into the rendering engine
    context_dict = {}

    try:
        
        # Attempt to find a category name slug with the given name.
        # If we can't, the .get() method raises a DoesNotExist Exception.
        # So the .get() method returns one model instance or raises an exception

        # return the category object with slug field entry category_name_slug
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the pages that are associated with this category
        pages = Page.objects.filter(category=category)


        # This adds our results to the template context under the name pages
        context_dict['pages'] = pages

        # We also add the category object to the context dictionary so that we can
        # use it to verify the category exists inside the template.
        context_dict['category'] = category

    except Category.DoesNotExist:

        # We get here if we didnt find the specified category
        # Don't do anything - The template will display the "no category" message for us.
        
        context_dict['pages'] = None
        
        context_dict['category'] = None

    # render the response and return it to the client with the template and the context dictionary
    return render(request, 'rango/category.html', context_dict)




def add_category(request):

    form = CategoryForm()

    # A HTTP POST? - this checks to see if the HTTP request was a POST request,
    # which if it was means that the user submitted data via the form.
    # if this is not the case then the next statement executed will be the rendering of the view
    # with the template and context dictionary displaying the empty form to the user for them to
    # enter their data. 
    if request.method == 'POST':

        form = CategoryForm(request.POST)

        # Check to see if the form is valid
        if form.is_valid():

            # save the new category to the database 
            form.save(commit=True)

            # Now the category is saved we could give a confirmation message,
            # but since the most recent category added is on the index page we
            # can redirect the user back to the index page so they can see their
            # form has been submitted successfully.
            return index(request)
        
        else:
            
            # The supplied form must contain some errors
            # These therefore should be printed to the terminal
            print(form.errors)

    # This will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any) supplying the template that will
    # be used within the view and the context didctionary.
    # This redirects the user to the view but displays an error message to the
    # user allowing them to resubmit after fixing the error, or gives a blank form
    # allowing them to enter their data.
    return render(request, 'rango/add_category.html', {'form':form})




def add_page(request, category_name_slug):

    # Attempt to find the given category object that the page about
    # to be added will be associated with
    try:

        # if it is found then assign it to category
        category = Category.objects.get(slug=category_name_slug)

    # otherwise if the category doesnt exist and a DoesNotExist exception occurs

    except Category.DoesNotExist:

    # then assign None to category
        category = None

    form = PageForm()

    # if the user has submitted the form and it contains data resulting in a POST request 
    if request.method == 'POST':

        # assign the submitted form with its data to the variable form 
        form = PageForm(request.POST)

        # if the form submitted contains valid data then 
        if form.is_valid():

            # if the category exists (is not None) then
            if category:

                page = form.save(commit=False)

                # give values to the hidden fields and then save:
                
                # assign category to the field category in the page
                page.category = category

                # assign the value 0 to the views field 
                page.views = 0

                # save the new page in the database 
                page.save()

                # redirect the user to the show_category view which will show the pages associated
                # with the category that the new page they have just added is one of, allowing them
                # to see that their page has been added to the database succesfully. 
                return show_category(request, category_name_slug)

        # Otherwise print the relevant error message 
        else:
            
            print(form.errors)

    # create the context dictionary that will be passed into the template for the add_page view 
    context_dict = {'form':form, 'category':category}

    # This will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any) supplying the template that will
    # be used within the view and the context didctionary.

    # This redirects the user to the add_page view but displays an error message to the
    # user allowing them to resubmit after fixing the error(s) they have made when submitting previously,
    # or gives a blank form for them to enter their data.
    return render(request, 'rango/add_page.html', context_dict)

            
            
        
            
            

        


    
