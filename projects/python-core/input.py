# Import necessary modules

# Define class
class Vehicle:
    def __init__(self, id, name, color, price, brand, type, yearOfManufacture):
        self.id = id
        self.name = name
        self.color = color
        self.price = price
        self.brand = brand
    
    @staticmethod
    def display_vehicle_info(vehicle):
        print(f"Vehicle ID: {vehicle.id}")
        print(f"Name: {vehicle.name}")
        print(f"Color: {vehicle.color}")
        print(f"Price: {vehicle.price}")
        print(f"Brand: {vehicle.brand}")