from typing import List, Dict

from django.db import models


class BaseModel:
    @classmethod
    def create(cls, items: List[Dict]) -> None:
        items = [cls(**item) for item in items]
        cls.objects.bulk_create(items)


class Genre(BaseModel, models.Model):
    name = models.CharField(max_length=255)


class Actor(BaseModel, models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
