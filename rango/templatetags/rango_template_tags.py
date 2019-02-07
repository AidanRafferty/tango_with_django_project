from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html')

# This method returns a list of categories, but is mashed up with the template
# rango/cats.html.

def get_category_list(cat=None):
    
    # return the categories along with the formatting
    # defined in the template rango/cats.html
    # cat refers to the actual category that is being viewed currently
    # which can optionally be passed into the function if the user is currently
    # accessing the show_category view or any other view in which a category object
    # Is currently being accessed - eg Add Page. The category they are viewing will then
    # be passed into the function.
    return {'cats':Category.objects.all(),
            'act_cat':cat}
