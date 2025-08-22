'''
from car import Car
from electric_car import ElectricCar

my_car = Car('奥迪', 'A6', '2025')

print(my_car.get_descriptive_name())

my_leaf = ElectricCar('福特', '野马', 2019)

print(my_leaf.get_descriptive_name())
'''
#使用别名
from car import Car
from electric_car import ElectricCar as Ec

my_car = Car('奥迪', 'A6', '2025')

print(my_car.get_descriptive_name())

my_leaf = Ec('福特', '野马', 2019)

print(my_leaf.get_descriptive_name())