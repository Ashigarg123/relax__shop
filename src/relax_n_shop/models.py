
from django.db import models
from django.db.models.deletion import CASCADE

from django.core.validators import MinValueValidator


# Create your models here.


class Product(models.Model):
    #pic=models.ImageField(upload_to = "images", null=True, blank=True)
    #url= models.URLField(max_length=300, null=True)
    title = models.CharField(max_length = 200)
    description  = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="allproducts/",null=True, blank=True)

    cr_date = models.DateTimeField(auto_now_add=True)
    Price = models.IntegerField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, default="vehicle", choices=(("Gadget", "Gadget"), ("Phone","Phone"), ("Fashion", "Fashion"), ("Furniture", "Furniture"), ("vehicle","vehicle"),("Home","Home")))



    def __str__(self):
        #return 'Posted on category- {} with title {}'.format(self.category, self.title)
        return self.title
