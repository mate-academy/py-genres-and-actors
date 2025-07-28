import pytest
from db.models import Genre

@pytest.mark.django_db
def test_genre_empty():
    
    assert Genre.objects.count() == 0

@pytest.mark.django_db
def test_create_genre():
    Genre.objects.create(name="Action")
    assert Genre.objects.filter(name="Action").exists()
