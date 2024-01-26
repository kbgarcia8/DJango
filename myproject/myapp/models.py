from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length =100) 
    #CharField takes string characters, there are other *Field syntax depending on your variable
    details = models.CharField(max_length =500)