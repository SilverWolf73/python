#1.Car类
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"

        return long_name.title()

my_new_car = Car('奥迪', 'a4', '1999')

print(my_new_car.get_descriptive_name())
'''
#2.给属性指定默认值
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"这辆车已经开了{self.odometer_reading}米")

my_new_car = Car('奥迪', 'a4', '1999')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
'''
#3.修改属性值
##1.直接修改
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"这辆车已经开了{self.odometer_reading}米")

my_new_car = Car('奥迪', 'a4', '1999')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
'''
##2.通过方法修改
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self,mileage):
        self.odometer_reading = mileage

    def read_odometer(self):
        print(f"这辆车已经开了{self.odometer_reading}米")

my_new_car = Car('奥迪', 'a4', '1999')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
'''
##3.通过方法让属性值递增
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def increas_odometer(self,mileage):
        self.odometer_reading += mileage

    def read_odometer(self):
        print(f"这辆车已经开了{self.odometer_reading}米")

my_new_car = Car('奥迪', 'a4', '1999')
print(my_new_car.get_descriptive_name())
my_new_car.increas_odometer(23_500)
my_new_car.read_odometer()