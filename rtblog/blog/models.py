from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


#https://pypi.prg/project/django-tinymce/
# Create your models here.

# CATEGORY MODEL

class Category(models.Model):
    Cat_id = models.AutoField(primary_key=True)
    Title=models.CharField(max_length=100)
    Description=models.TextField()
    Url = models.CharField(max_length=100)

    Image = models.ImageField(upload_to='category/')
    Add_date = models.DateField(auto_now_add=True,null=True)
# here i create a function for show min admin area with picture view...
    def Image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px;border-radius:50%;"/>'.format(self.Image))

    def __str__(self):
        return self.Title
 # End Category Models


 # POST MODEL



class Post(models.Model):
     Post_id = models.AutoField(primary_key=True)
     Title = models.CharField(max_length=200)
     Content = HTMLField()
     url = models.CharField(max_length=100)
     Cat = models.ForeignKey(Category,on_delete=models.CASCADE)
     Images = models.ImageField(upload_to='post/')

     def __str__(self):
         return self.Title