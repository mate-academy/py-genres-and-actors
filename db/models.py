from django.db import models

class Genre(model.Model):
    name = models.CharField(max_length=255)
    
class Actor(model.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
