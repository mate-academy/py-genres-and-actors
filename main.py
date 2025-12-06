from django.db.models.query import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet[Actor]:
    Genre.objects.get_or_create(name="Western")
    Genre.objects.get_or_create(name="Action")
    Genre.objects.get_or_create(name="Drama")

    Actor.objects.get_or_create(first_name="George", last_name="Clooney")
    Actor.objects.get_or_create(first_name="Keanu", last_name="Reeves")
    Actor.objects.get_or_create(first_name="Will", last_name="Smith")
    Actor.objects.get_or_create(first_name="Jaden", last_name="Smith")

    Genre.objects.filter(name="Action").delete()

    queryset: QuerySet[Actor] = (
        Actor.objects.filter(last_name="Smith").order_by("first_name")
    )

    return queryset
