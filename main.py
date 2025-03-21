import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


# Клас Car
class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


# Клас CarWashStation
class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rate: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (total_rating + rate) / self.count_of_ratings, 1
        )


# Реалізація функції main
def main() -> QuerySet:
    # Створюємо жанри
    Genre.objects.get_or_create(name="Western")
    Genre.objects.get_or_create(name="Drama")

    # Створюємо акторів
    Actor.objects.get_or_create(first_name="George", last_name="Clooney")
    Actor.objects.get_or_create(first_name="Keanu", last_name="Reeves")
    Actor.objects.get_or_create(first_name="Will", last_name="Smith")
    Actor.objects.get_or_create(first_name="Jaden", last_name="Smith")

    # Повертаємо список акторів для перевірки тестами
    return Actor.objects.filter(
        first_name__in=["Jaden", "Will"]).order_by("first_name")


if __name__ == "__main__":
    actors = main()
    for actor in actors:
        print(f"{actor.first_name} {actor.last_name}")
