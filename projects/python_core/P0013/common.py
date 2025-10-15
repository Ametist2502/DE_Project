import random
import timeit
import pandas as pd
import os

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    return wrapper

class Common:
    @staticmethod
    @timer
    def generate_random_list(n: int, lower_bound: int = 1, upper_bound: int = 100) -> list:
        """"Generate a list of n random integers within spectified bounds."""
        list_of_numbers = [random.randint(lower_bound, upper_bound) for _ in range(n)]
        return list_of_numbers
    
class FileHandler:
    @staticmethod
    @timer
    def read_csv(file_path: str) -> pd.DataFrame:
        """Read a CSV file and return a pandas DataFrame."""
        df = pd.read_csv(file_path)
        return df
    
    @staticmethod
    @timer
    def write_csv(df: pd.DataFrame, file_path: str):
        """Write a pandas DataFrame to a CSV file."""
        file_exists = os.path.exists(file_path)
        df.to_csv(file_path, index=False, mode='a', header=not file_exists)