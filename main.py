import init_django_orm  # noqa: F401

from django.db.models import QuerySet


from db.models import Actor, Genre


def main() -> QuerySet:
    genres = [
        ("Western",),
        ("Action",),
        ("Dramma",),
    ]

    for (name,) in genres:
        Genre.objects.create(name=name)

    action = Genre.objects.get(name="Action")
    dramma = Genre.objects.get(name="Dramma")

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    george = Actor.objects.get(first_name="George", last_name="Klooney")
    kianu = Actor.objects.get(first_name="Kianu", last_name="Reaves")

    dramma.name = "Drama"
    dramma.save()

    george.last_name = "Clooney"
    george.save()

    kianu.last_name = "Reeves"
    kianu.first_name = "Keanu"
    kianu.save()

    action.delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
