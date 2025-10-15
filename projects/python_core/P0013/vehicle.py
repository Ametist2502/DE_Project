# Import necessary modules
import uuid
from abc import ABC, abstractmethod


# Define class Vehicle
class Vehicle:
    def __init__(self, name, color, price, brand):
        self._id = str(uuid.uuid4())
        self._name = name
        self._color = color
        self._price = price
        self._brand = brand
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        self._color = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value

    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, value):
        self._brand = value
    
    @abstractmethod
    def display_vehicle_info(self):
        pass

class Car(Vehicle):
    def __init__(self, name, color, price, brand, type, yearOfManufacture):
        super().__init__(name, color, price, brand)
        self._type = type
        self._yearOfManufacture = yearOfManufacture
    
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, value):
        self._type = value
    
    @property
    def yearOfManufacture(self):
        return self._yearOfManufacture
    
    @yearOfManufacture.setter
    def yearOfManufacture(self, value):
        self._yearOfManufacture = value

    def display_vehicle_info(self):
        return (f"Car ID: {self._id}, Name: {self._name}, Color: {self._color}, "
                f"Price: {self._price}, Brand: {self._brand}, Type: {self._type}, Year of Manufacture: {self._yearOfManufacture}")
    
    def to_dict(self):
        return {
            "ID": self._id,
            "Name": self._name,
            "Color": self._color,
            "Price": self._price,
            "Brand": self._brand,
            "Type": self._type,
            "YearOfManufacture": self._yearOfManufacture
        }
    
class Motorcycle(Vehicle):
    def __init__(self, name, color, price, brand, speed, licenseRequired: bool):
        super().__init__(name, color, price, brand, speed, licenseRequired)
        self._speed = speed
        self._licenseRequired = licenseRequired
    
    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, value):
        self._speed = value
    
    @property
    def licenseRequired(self):
        return self._licenseRequired
    @licenseRequired.setter
    def licenseRequired(self, value):
        self._licenseRequired = value

    def display_vehicle_info(self):
        return (f"Motorcycle ID: {self._id}, Name: {self._name}, Color: {self._color}, "
                f"Price: {self._price}, Brand: {self._brand}, Speed: {self._speed}, licenseRequired: {self._licenseRequired}")
    
    def to_dict(self):
        return {
            "ID": self._id,
            "Name": self._name,
            "Color": self._color,
            "Price": self._price,
            "Brand": self._brand,
            "Speed": self._speed,
            "LicenseRequired": self._licenseRequired
        }

    
    