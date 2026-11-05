from abc import ABC, abstractmethod
from exceptions import InvalidInputError, NegativeDistanceError


# Abstract Parent Class
class Vehicle(ABC):

    def __init__(self, driver_name, rating):
        self.driver_name = driver_name
        self.rating = rating

# Property and setter for vehicle ratings
    @property
    def rating(self):
        return self._rating

# Setter
    @rating.setter
    def rating(self, value):
        if value < 1 or value > 5:
            raise InvalidInputError("Rating must be between 1 and 5.")

        self._rating = value

 # Validate distance
    def validate_distance(self, distance):
        if distance < 0:
            raise NegativeDistanceError("Distance cannot be negative.")

# Abstract method
    @abstractmethod
    def calculate_fare(self, distance):
        pass
   
# child classes Bike and Car
class Bike(Vehicle):

    def calculate_fare(self, distance):
        self.validate_distance(distance)

        rate = 15
        return distance * rate

class Car(Vehicle):

    def calculate_fare(self, distance):
        self.validate_distance(distance)

        rate = 25
        return distance * rate
