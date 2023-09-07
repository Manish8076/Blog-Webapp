from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class ContactUsTb(models.Model):
     name = models.CharField(max_length=50)
     email = models.CharField(max_length=90)
     phone = models.IntegerField()
     address = models.CharField(max_length=90)
     message = models.TextField()
     created_at = models.DateTimeField( auto_now_add=True)
     
     
     
     def __str__(self) ->str:
        return self.name


     
class popularblog(models.Model):
     title = models.CharField(max_length=122)
     author = models.CharField(max_length=90)
     posted_date = models.DateField(auto_now_add=True)
     content= RichTextField()
     created_at = models.DateTimeField(auto_now_add=True)
     
     
class allblog(models.Model):
     title = models.CharField(max_length=122)
     author = models.CharField(max_length=90)
     posted_date = models.DateField(auto_now_add=True)
     content= RichTextField()
     created_at = models.DateTimeField(auto_now_add=True)
     
               

          