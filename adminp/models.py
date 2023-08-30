from django.db import models

# Create your models here.

class Property(models.Model):
    pname = models.CharField(max_length=300)
    plocation = models.CharField(max_length=300)
    pdimension = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    coverimage = models.ImageField(upload_to='photos/projects',default='photos/projects/noimage.png')
    

class Photos(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/projects',default='photos/projects/noimage.png')
    
class Amenities(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    data = models.CharField(max_length=300)
    
class Contact(models.Model):
    message = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    number = models.CharField(max_length=500)
    mark = models.BooleanField(default=False)