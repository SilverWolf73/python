#一个模块导入多个类
'''
from Car import Car, ElectricCar

my_car = Car('奥迪', 'A6', '2025')
print(my_car.get_descriptive_name())
my_leaf = ElectricCar('特斯拉', 's1', '2019')
print(my_leaf.get_descriptive_name())
'''
#导入整个模块
'''
import Car

my_car = Car.Car('奥迪', 'A6', '2025')
print(my_car.get_descriptive_name())
my_leaf = Car.ElectricCar('特斯拉', 's1', '2019')
print(my_leaf.get_descriptive_name())
'''
#导入模块所有类
from Car import *

my_car = Car('奥迪', 'A6', '2025')
print(my_car.get_descriptive_name())
my_leaf = ElectricCar('特斯拉', 's1', '2019')
print(my_leaf.get_descriptive_name())