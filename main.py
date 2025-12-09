import os
import django
from db.models import Genre, Actor

from django.urls import path

# Zgodnie z wymaganiem, urlpatterns jest zachowane, jeśli jest częścią struktury projektu
urlpatterns = []


def main():
    # Dane do utworzenia obiektów Genre i Actor
    genres_to_create = ["Western", "Dramma", "Action"]

    actors_to_create = [
        ("George", "Klooney", False),
        ("Kianu", "Reaves", False),
        ("Scarlett", "Keegan", True),
        ("Will", "Smith", False),
        ("Jaden", "Smith", False),
        ("Scarlett", "Johansson", True),
    ]

    # CHECKLIST ITEM #2 & #3: Refaktoryzacja tworzenia obiektów Genre za pomocą pętli
    for name in genres_to_create:
        Genre.objects.create(name=name)

    # CHECKLIST ITEM #2 & #3: Refaktoryzacja tworzenia obiektów Actor za pomocą pętli
    for first_name, last_name, is_actress in actors_to_create:
        Actor.objects.create(first_name=first_name, last_name=last_name, is_actress=is_actress)

    # Pozostała logika bazodanowa
    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")

    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()

    Actor.objects.filter(is_actress=True, first_name="Scarlett").delete()

    smith_actors = Actor.objects.filter(last_name="Smith").order_by('first_name')

    return smith_actors
