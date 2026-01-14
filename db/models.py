from typing import List, Dict

from django.db import models


class BaseModel:
    @classmethod
    def create(cls, items: List[Dict]) -> None:
        items = [cls(**item) for item in items]
        cls.objects.bulk_create(items)


class Genre(BaseModel, models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return (
            f"Genre (name='{self.name}')"
        )


class Actor(BaseModel, models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return (
            "Actor "
            f"(first_name='{self.first_name}', "
            f"last_name='{self.last_name}')"
        )
