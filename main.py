# main.py
from _init_Django_orm import *
from db.models import Genre, Actor


def main():
    """Create, update, delete records and return actors with last name 'Smith'."""
    # CREATE genres
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    dramma = Genre.objects.create(name="Dramma")

    # CREATE actors
    george = Actor.objects.create(first_name="George", last_name="Klooney")
    kianu = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    will = Actor.objects.create(first_name="Will", last_name="Smith")
    jaden = Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # UPDATE records
    dramma.name = "Drama"
    dramma.save()

    george.last_name = "Clooney"
    george.save()

    kianu.first_name = "Keanu"
    kianu.last_name = "Reeves"
    kianu.save()

    # DELETE records
    Genre.objec
