class Vehicle:
    brand = ""
    year = 0
    
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"VEHICLE DETAILS:\n BRAND: {self.brand};\n YEAR: {self.year}")

class Car(Vehicle):
    fuel_type = ""

    def __init__(self, brand, year, fuel_type : str):
        super().__init__(brand, year)
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f" FUEL TYPE: {self.fuel_type}")

