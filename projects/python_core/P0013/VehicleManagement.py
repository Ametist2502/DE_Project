from vehicle import Car, Motorcycle
from common import timer, Common, FileHandler
import pandas as pd


class VehicleManagement:
    def __init__(self):
        self.vehicles = []

    @timer
    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, (Car, Motorcycle)):
            raise ValueError("Vehicle must be an instance of Car or Motorcycle")
        self.vehicles.append(vehicle)

    @timer
    def list_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle.display_vehicle_info())

    @timer
    def save_vehicles_to_csv(self, file_path: str):
        data = [vehicle.to_dict() for vehicle in self.vehicles]
        df = pd.DataFrame(data)
        FileHandler.write_csv(df, file_path)
        self.vehicles.clear()

    @timer
    def load_vehicles_from_csv(self, file_path: str):
        df = FileHandler.read_csv(file_path)
        print(df)