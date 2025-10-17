from common import timer, Common, FileHandler
from vehicle import Car, Motorcycle
import pandas as pd
from VehicleManagement import VehicleManagement

def main():
    vm = VehicleManagement()
    while True:
        print("Vehicle Management System")
        print("=========================")
        print("1. Add Vehicle")
        print("2. List Vehicles")
        print("3. Save Vehicles to CSV")
        print("4. Load Vehicles from CSV")
        print("5. Exit")
        option = int(input("Select an option: "))
        if option == 1:
            vehicle_type = input("Enter vehicle type (car/motorcycle): ").strip().lower()
            name = input("Enter name: ")
            color = input("Enter color: ")
            price = int(input("Enter price: ")) 
            brand = input("Enter brand: ")
            if vehicle_type == "car":
                type = input("Enter car type (e.g., sedan, SUV): ")
                yearOfManufacture = int(input("Enter year of manufacture: "))
                car = Car(name, color, price, brand, type, yearOfManufacture)
                vm.add_vehicle(car)
            elif vehicle_type == "motorcycle":
                speed = int(input("Enter speed (km/h): "))
                licenseRequired = bool(input("Enter licenes required: "))
                motorcycle = Motorcycle(name, color, price, brand, speed, licenseRequired)
                vm.add_vehicle(motorcycle)
            else:
                print("Invalid vehicle type.")
        elif option == 2:
            # vm = VehicleManagement()
            vm.list_vehicles()
        elif option == 3:
            # vm = VehicleManagement()
            # file_path = input("Enter file path to save CSV: ")
            vehicle_type = input("Enter vehicle type (car/motorcycle): ").strip().lower()
            if vehicle_type == "car":
                file_path = "data/car.csv"
            elif vehicle_type == "motorcycle":
                file_path = "data/motorcycle.csv"
            else:
                print("Invalid vehicle type.")
                continue
            vm.save_vehicles_to_csv(file_path)
            vehicle_type = ""
        elif option == 4:
            # vm = VehicleManagement()
            # file_path = input("Enter file path to load CSV: ")
            vehicle_type = input("Enter vehicle type (car/motorcycle): ").strip().lower()
            if vehicle_type == "car":
                file_path = "data/car.csv"
            elif vehicle_type == "motorcycle":
                file_path = "data/motorcycle.csv"
            else:
                print("Invalid vehicle type.")
                continue
            vm.load_vehicles_from_csv(file_path)    
        elif option == 5:
            print("Exiting the program.")
            return False
        pass


if __name__ == "__main__":
    main()