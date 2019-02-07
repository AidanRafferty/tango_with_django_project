from django import forms
from rango.models import Page, Category
# Here we implement the necessary infrastructure that will allow users to add categories
# and pages to the database via forms


# This class inherits from ModelForm which allows us to create forms from a pre-existing model
class CategoryForm(forms.ModelForm):

    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    slug = forms.CharField(widget=forms.HiddenInput(), required=False)


    # This is an inline class to provide additional information on the form
    class Meta:
        # Provide an association between the ModelForm and the Category Model
        model = Category
        fields = ('name', )


class PageForm(forms.ModelForm):
    
    
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    
    url = forms.CharField(max_length=200,
                         help_text="Please enter the URL of the page.")

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # Override the clean() method, which is called before saving form data to a
    # new model instance, allowing us to insert code which can verify and even fix
    # any form data the user inputs. For example we can check that the url entered begins with
    # http:// and if not we can add this to the front of it.
    def clean(self):
        
        cleaned_data = self.cleaned_data

        url = cleaned_data.get('url')

        # if the url is not empty and doesnt start with http:// then prepend it to the url
        if url and not url.startswith('http://'):

            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        
        # Provide an association between the ModelForm and the Page Model
        model = Page

        # We exclude this field, category, as this is the foreign key and so this
        # is hidden in the form and is not shown to the user. 
        exclude = ('category',)


        
# within the clean() method a simple pattern is followed which you can replicate to form your own
# Django form handling code.
# 1. Form data is obtained from the ModelForm dictionary attribute cleaned_data

# 2. Form fields that you wish to check can then be taken from the cleaned_data dictionary. Use
# the .get() method provided by the dictionary object to obtain the form’s values. If a user
# does not enter a value into a form field, its entry will not exist in the cleaned_data
# dictionary.

# 3. For each form field that you wish to process, check that a value was retrieved. If something
# was entered, check what the value was. If it isn’t what you expect, you can then add some
# logic to fix this issue before reassigning the value in the cleaned_data dictionary. eg adding the
# correct start of a url.

# 4. You must always end the clean() method by returning the reference to the cleaned_data
# dictionary. Otherwise the changes won’t be applied.

