class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def updata_odometer(self,mileage):
        if mileage > 0:
            self.odometer_reading += mileage
        else :
            print("禁止修改里程数")

    def increas_odometer(self, mileage):
        self.odometer_reading += mileage

    def read_odometer(self):
        print(f"这辆车已经开了{self.odometer_reading}米")

    def fill_gas_tank(self,liter):
        self.liter = liter
        print(f"还有{self.liter}升油")