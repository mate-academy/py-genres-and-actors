from django.core.management import execute_from_command_line
import os
import sys

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "py-genres-and-actors.settings")

# Importar modelos
from db.models import Genre, Actor

def main():
    # Crear géneros
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Acción")
    Genre.objects.create(name="Drama")

    # Crear actores
    Actor.objects.create(first_name="George", last_name="Clooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # Actualizar géneros y actores
    Genre.objects.filter(name="Dramma").update(name="Drama")  # No hay "Dramma" creado, pero si existiera...
    Genre.objects.filter(name="Drama").update(name="Drama")  # Esto no haría nada en este caso
    Actor.objects.filter(first_name="George", last_name="Clooney").update(last_name="Clooney")  # Esto no haría nada en este caso
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

    # Actualizar George Clooney
    Actor.objects.filter(first_name="George", last_name="Clooney").update(last_name="Clooney")

    # Actualizar a Keanu Reeves
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

    # Borrar género Acción
    Genre.objects.filter(name="Acción").delete()

    # Borrar actrices con first_name "Scarlett"
    Actor.objects.filter(first_name="Scarlett").delete()

    # Devolver QuerySet de actores con last_name "Smith" y ordenados por first_name
    return Actor.objects.filter(last_name="Smith").order_by('first_name')

if __name__ == "__main__":
    # execute_from_command_line(sys.argv)
    print(main())
    print(Genre.objects.all())
    print(Actor.objects.all())