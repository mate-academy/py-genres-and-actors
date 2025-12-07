import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
	Genre.objects.create(name="Western")
	Genre.objects.create(name="Action")
	Genre.objects.create(name="Dramma")

	Actor.objects.create(first_name="George", last_name="Klooney")
	Actor.objects.create(first_name="Kianu", last_name="Reaves")
	Actor.objects.create(first_name="Scarlett", last_name="Keegan")
	Actor.objects.create(first_name="Will", last_name="Smith")
	Actor.objects.create(first_name="Jaden", last_name="Smith")
	Actor.objects.create(first_name="Scarlett", last_name="Johansson")

	dramma = Genre.objects.get(name="Dramma")
	dramma.name = "Drama"
	dramma.save()

	george_klooney = Actor.objects.get(first_name="George", last_name="Klooney")
	george_klooney.last_name = "Clooney"
	george_klooney.save()

	kianu_reaves = Actor.objects.get(first_name="Kianu", last_name="Reaves")
	kianu_reaves.first_name = "Keanu"
	kianu_reaves.last_name = "Reeves"
	kianu_reaves.save()

	Genre.objects.get(name="Action").delete()

	Actor.objects.filter(first_name="Scarlett").delete()

	smith_actors_queryset = Actor.objects.filter(last_name="Smith").order_by("first_name")

	return smith_actors_queryset
