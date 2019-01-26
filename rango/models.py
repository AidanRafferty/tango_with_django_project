from django.db import models

# Create your models here.
class Category(models.Model):

    # only one field in this model, unique as is the primary key
    name = models.CharField(max_length =128, unique = True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        #return "%s-%d-%d"%(self.name, self.views, self.likes)
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

    
