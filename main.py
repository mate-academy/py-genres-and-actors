import init_django_orm  # noqa: F401
from db.models import Genre
from db.models import Actor


def add(manager, **kwargs):
    manager.create(**kwargs)


def delete(manager, **kwargs):
    manager.filter(**kwargs).delete()


def get(manager, **kwargs):
    return manager.filter(**kwargs).get()


def update(manager, **kwargs):
    manager.update(**kwargs)


def filter_manager(manager, **kwargs):
    return manager.filter(**kwargs)


def main():
    man_genre = Genre.objects
    man_actor = Actor.objects
    add(man_genre, name="Western")
    add(man_genre, name="Action")
    add(man_genre, name="Dramma")
    add(man_actor, first_name="George", last_name="Klooney")
    add(man_actor, first_name="Kianu", last_name="Reaves")
    add(man_actor, first_name="Scarlett", last_name="Keegan")
    add(man_actor, first_name="Will", last_name="Smith")
    add(man_actor, first_name="Jaden", last_name="Smith")
    add(man_actor, first_name="Scarlett", last_name="Johansson")
    print(man_genre.all())
    filter_man = filter_manager(man_genre, name="Dramma")
    update(filter_man, name="Drama")
    print(man_genre.all())

    print(man_actor.all())
    filter_man = filter_manager(man_actor, last_name="Klooney")
    update(filter_man, last_name="Clooney")
    filter_man = filter_manager(man_actor,
                                first_name="Kianu",
                                last_name="Reaves")
    update(filter_man, first_name="Keanu", last_name="Reeves")
    delete(man_genre, name="Action")
    delete(man_actor, first_name="Scarlett")
    print(man_actor.all())
    return man_actor.filter(last_name="Smith").order_by("first_name").all()
