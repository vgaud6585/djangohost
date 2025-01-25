from django.db import models

# Create your models here.

class User(models.Model):
   usr_name = models.CharField(max_length=100)
   usr_age = models.IntegerField()
   usr_image = models.ImageField(upload_to='images/')

   def __str__(self):
       return self.usr_name