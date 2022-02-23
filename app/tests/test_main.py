import pytest

from ..main import main, Genre, Actor


@pytest.mark.django_db
def test_main():
    actors = main()
    assert list(actors.values_list("first_name", "last_name")) == [
        ("Jaden", "Smith"),
        ("Will", "Smith"),
    ]


@pytest.mark.django_db
def test_genres():
    main()
    assert list(Genre.objects.values_list("name")) == [
        ("Western",),
        ("Drama",),
    ]


@pytest.mark.django_db
def test_actors():
    main()
    assert list(Actor.objects.values_list("first_name", "last_name")) == [
        ("George", "Clooney"),
        ("Keanu", "Reeves"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
    ]
