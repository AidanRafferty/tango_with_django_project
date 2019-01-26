# This script is used to populate the database with data that is realistic and
# credible so that we do not have to go in and enter the sample data ourselves manually

# This script is referred to as a population script as a result.

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page


# get_or_create() - avoids creating duplicates - returns a tuple (object, created) - created T/F
# so the get_or_create()[0] - returns only the object reference as this is the first element in the
# tuple

def populate():

    # First we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem confusing, but this allows us to iterate over each data
    # structure, and add the data to our models.


    # These lists of dictionaries contain the pages from each category
    python_pages = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/"},
        {"title":"How to Think like a Computer Scientist",
        "url":"http://www.greenteapress.com/thinkpython/"},
        {"title":"Learn Python in 10 Minutes",
        "url":"http://www.korokithakis.net/tutorials/python/"} ]

    django_pages = [
        {"title":"Official Django Tutorial",
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title":"Django Rocks",
         "url":"http://www.djangorocks.com/"},
        {"title":"How to Tango with Django",
         "url":"http://www.tangowithdjango.com/"} ]

    other_pages = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask",
         "url":"http://flask.pocoo.org"} ]

    # This dictionary of dictionaries of our categories pages contains
    # the category as the key and the value as
    # the dictionary containing the key "pages" and the value being the
    # dictionary of the pages of that category
    
    cats = {"Python": {"pages": python_pages, "views":128, "likes":64},
            "Django": {"pages": django_pages, "views":64, "likes":32},
            "Other Frameworks": {"pages": other_pages, "views":32, "likes":16}}





    # cat means category, with cat_data referring to the dictionary of the pages
    # of this category

    # loop through the keys and values in the cats dictionary, with cat storing
    # the current keys and cat_data storing the current value being iterated over
    for cat, cat_data in cats.items():

        # attempt to create a new Category object with the current key in the cats dictionary
        # and store the new object, or current object with the same attributes, in c
        c = add_cat(cat, cat_data["views"], cat_data["likes"])

        # loop through the dictionary of pages details for the current category
        for p in cat_data["pages"]:

            # Attempt to create a new page record by supplying the category object the page is related to as the foreign key in order to maintain a 1 to many relationship
            # between Category and Pages, as 1 Category can be the type of category of many pages, but a is of only 1 category.
            # so supply the category record(category) that this page is associated with - eg if the page is of category Python, then supply the Python record from
            # the Category model. Then supply the other page attribute details in order to fill the remaining fields for the page, being it's title and URL. 
            add_page(c, p["title"], p["url"])


    # loop through each of the category objects, c, that have been added 
    for c in Category.objects.all():
        
        # create an inner loop through the page objects of category c,
        # using the filter functionality
        for p in Page.objects.filter(category=c):

            # print the current category alongside the current page of that category 
            print("- {0} - {1}".format(str(c), str(p)))

            



# Create a function that creates a new page object and adds this to the database
def add_page(cat, title, url, views=0):

    # either return an existing page object with the same attributes supplied,
    # or create a page object using the peramters supplied, using the Category object related to
    # the page as the foreign key.
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    print("This is what is held in the category field in page record", p.category)

    # if the object has to be created then assign the values passed into the function
    # to their respective attributes 
    p.url = url
    p.views = views
    p.save()
    return p






# This is effectively a constructor for category objects
# which returns an object with the same name attribute or creates a new Category
# object with the name peramter set as the value for the name field. 
def add_cat(name, views, likes):
  
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    
    # Save the database entry
    c.save()

    print(c,"-",c.views,"-",c.likes)
    

    # return the new Category object
    return c


# This is where the execution begins

# The __name__ == '__main__' trick allows a Python module to act as
# either a reusable module or a standalone Python script.

# A reusable module is one that can be imported into other modules (e.g. through an import statement), while
# and  standalone Python script would be executed from a terminal/Command Prompt by
# entering python module.py.

# This peice of code therefore ensures that the population script can only be executed
# when this module is ran as a standalone python script. This means that the populate()
# function wont be called unless the module is ran on its own, as this is the only time __name__ will == '__main__' and so will not be ran
# if the module is imported into another module and called from there, as __name__
# will contain the name of the python module that has imported this module, and so
# wont satisfy the if condition.


if __name__ == '__main__':

    print("Starting Rango population script...")

    populate()
    






    
