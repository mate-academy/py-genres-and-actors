# db/models.py
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)

class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

# main.py
from db.models import Genre, Actor

def main():
    # Create genres and actors
    Genre.objects.bulk_create([
        Genre(name="Western"),
        Genre(name="Action"),
        Genre(name="Dramma"),
    ])
    
    Actor.objects.bulk_create([
        Actor(first_name="George", last_name="Klooney"),
        Actor(first_name="Kianu", last_name="Reaves"),
        Actor(first_name="Scarlett", last_name="Keegan"),
        Actor(first_name="Will", last_name="Smith"),
        Actor(first_name="Jaden", last_name="Smith"),
        Actor(first_name="Scarlett", last_name="Johansson"),
    ])
    
    # Update records
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu", last_name="Reeves"
    )
    
    # Delete records
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    
    # Return QuerySet
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
