from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name


class Page(models.Model):

    # these are the fields in the model(the database table)
    # this is the foreign key of the Category model, allowing a 1 to many relationship
    # to be created between the Category and Page tables

    # This field holds the record in the Category 
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    # this method is used to return a string representation of the class
    # like the toString() in java
    def __str__(self):
        return self.title

class UserProfile(models.Model):

    # this line associates UserProfile to a user model instance in a 1 to 1
    # relationship

    user = models.OneToOneField(User)

    # add the 2 new additional attributes 
    website = models.URLField(blank=True)

    # we set blank to true so that the user is able to leave this field blank if
    # necessary
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Furthermore, it should be noted that the ImageField field has an upload_to attribute.
    # The value of this attribute is conjoined with the project’s MEDIA_ROOT
    # setting to provide a path with which uploaded profile images will be stored.
    # For example, a MEDIA_ROOT of <workspace>/tango_with_django_project/media/
    # and upload_to attribute of profile_images will result in all profile images
    # being stored in the directory <workspace>/tango_with_django_project/media/profile_images/.
    
    
    # create a toString method
    def __str__(self):
        return self.user.username
    
    
    
