from car import Car

class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"这辆车有{self.battery_size}度电")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self,liter):
        print("电车没有油箱")

    def describe_battery(self):
        print(f"还有{self.battery}度电")