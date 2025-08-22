from Car import ElectricCar

my_leaf = ElectricCar('福特', '野马', '2025')
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()