from django.db import models
from django.db.models.fields import EmailField

class Card(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    company = models.CharField(max_length=70)
    title = models.CharField(max_length=70)
    sideBusiness = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    country = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    
    def __str__(self):
        return self.first_name+" "+ self.last_name

