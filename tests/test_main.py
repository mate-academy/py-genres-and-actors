import pytest
from db.models import Genre, Actor
from main import main


@pytest.mark.django_db
def test_main_returns_correct_queryset() -> None:
    queryset = main()
    # Check if only Smiths are returned and sorted by first_name
    first_names = list(queryset.values_list("first_name", flat=True))
    assert first_names == ["Jaden", "Will"]
    for actor in queryset:
        assert actor.last_name == "Smith"


@pytest.mark.django_db
def test_genres_after_main() -> None:
    main()
    genres = list(
        Genre.objects.values_list("name", flat=True).order_by("name")
    )
    # Action should be deleted, Dramma updated to Drama
    assert genres == ["Drama", "Western"]


@pytest.mark.django_db
def test_actors_after_main() -> None:
    main()
    actors = list(Actor.objects.all().order_by("first_name"))
    # Verify name updates and deletion of all "Scarlett" entries
    assert len(actors) == 4

    names = [(a.first_name, a.last_name) for a in actors]
    assert ("George", "Clooney") in names
    assert ("Keanu", "Reeves") in names
    assert ("Will", "Smith") in names
    assert ("Jaden", "Smith") in names

    # Verify that Scarlett is no longer in the database
    assert Actor.objects.filter(first_name="Scarlett").count() == 0
