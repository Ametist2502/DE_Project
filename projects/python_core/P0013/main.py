from common import timer, Common, FileHandler
from vehicle import Car, Motorcycle
import pandas as pd
from VehicleManagement import VehicleManagement

def main():
    print("Vehicle Management System")
    print("=========================")
    print("1. Add Vehicle")
    print("2. List Vehicles")
    print("3. Save Vehicles to CSV")
    print("4. Load Vehicles from CSV")
    print("5. Exit")
    option = int(input("Select an option: "))
    if option == 1:
        vm = VehicleManagement()
        vehicle_type = input("Enter vehicle type (car/motorcycle): ").strip().lower()
        name = input("Enter name: ")
        color = input("Enter color: ")
        price = float(input("Enter price: "))
        brand = input("Enter brand: ")
        if vehicle_type == "car":
            type = input("Enter car type (e.g., sedan, SUV): ")
            year = int(input("Enter year of manufacture: "))
            car = Car(name, color, price, brand, type, year)
            vm.add_vehicle(car)
        elif vehicle_type == "motorcycle":
            engine_capacity = int(input("Enter engine capacity (cc): "))
            motorcycle = Motorcycle(name, color, price, brand, engine_capacity)
            vm.add_vehicle(motorcycle)
        else:
            print("Invalid vehicle type.")
    elif option == 2:
        vm = VehicleManagement()
        vm.list_vehicles()
    elif option == 3:
        vm = VehicleManagement()
        file_path = input("Enter file path to save CSV: ")
        vm.save_vehicles_to_csv(file_path)
    elif option == 4:
        vm = VehicleManagement()
        file_path = input("Enter file path to load CSV: ")
        vm.load_vehicles_from_csv(file_path)    
    elif option == 5:
        print("Exiting the program.")
    pass
    


if __name__ == "__main__":
    main()