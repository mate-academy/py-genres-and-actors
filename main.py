import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    print(Genre.objects.create(name="Western",))
    print(Genre.objects.create(name="Action",))
    print(Genre.objects.create(name="Dramma",))
    print(Genre.objects.all())
    print(Actor.objects.create(first_name="George", last_name="Klooney"))
    print(Actor.objects.create(first_name="Kianu", last_name="Reaves"))
    print(Actor.objects.create(first_name="Scarlett", last_name="Keegan"))
    print(Actor.objects.create(first_name="Will", last_name="Smith"))
    print(Actor.objects.create(first_name="Jaden", last_name="Smith"))
    print(Actor.objects.create(first_name="Scarlett", last_name="Johansson"))
    print(Actor.objects.all())
    print(Genre.objects.filter(name="Dramma", ).update(name="Drama", ))
    print(Actor.objects.filter(
        first_name="George", last_name="Klooney").update(
        last_name="Clooney", ))
    print(Actor.objects.filter(
        first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"))
    print(Genre.objects.filter(name="Action", ).delete())
    print(Actor.objects.filter(first_name="Scarlett").delete())
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
