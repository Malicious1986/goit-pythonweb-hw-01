from abc import ABC, abstractmethod
import logging

import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class VehicleFactory(ABC):
    region: str = ""

    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass

    def _get_region_spec(self, model: str) -> str:
        return f"{model} ({self.region})"


class USVehicleFactory(VehicleFactory):
    region = "US Spec"

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, self._get_region_spec(model))

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, self._get_region_spec(model))


class EUVehicleFactory(VehicleFactory):
    region = "EU Spec"

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, self._get_region_spec(model))

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, self._get_region_spec(model))


class Car(Vehicle):

    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):

    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Мотор заведено")


def main():
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()


if __name__ == "__main__":
    main()
