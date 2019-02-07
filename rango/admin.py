from django.contrib import admin
from rango.models import Category, Page
# Register your models here.

#admin.site.register(Category)

class PageAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)


# this ensures that the admin interface automatically prepopulates that slug field
# as you type in the category name, so you dont have to fill the field yourself.
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('name',)}

# update the registration to include this customised interface.
admin.site.register(Category, CategoryAdmin)


    
    
    
    
