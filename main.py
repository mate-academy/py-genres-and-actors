import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre

from db.models import Actor


def main() -> QuerySet:

    #Genre.objects.create(name="Dramma",)
    #Genre.objects.filter(name="Dramma").update(name="Drama")
    #Genre.objects.filter(name="Action").delete()
    print(Genre.objects.all())

    #Actor.objects.create(first_name="Scarlett", last_name="Johansson",)
    #Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")
    #Actor.objects.filter(first_name="Scarlett").delete()
    Actor_filter = Actor.objects.filter(last_name="Smith").order_by("first_name")
    #print(Actor.objects.all())
    print(Actor_filter)


if __name__ == "__main__":
    main()
