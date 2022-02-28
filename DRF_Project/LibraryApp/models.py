from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('successfully_added')

    
    

def pre_book_save(sender,instance,**kwargs):
    instance.name = instance.name.upper()
    instance.author = instance.author.capitalize()
    
pre_save.connect(pre_book_save,sender=Book)
     