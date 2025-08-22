class Restaurant:
    def __init__(self,restaurant_name, restaurant_type):
        self.name = restaurant_name
        self.type = restaurant_type

    def open_restaurant(self, open_time):
        self.open_time = open_time
        print(f"{self.open_time}点{self.name}开门了")

    def shut_restaurant(self,shut_time):
        self.shut_time = shut_time
        print(f"{self.shut_time}点{self.name}关门了")

    def introduse(self):
        print(f"{self.name}是{self.type}类型的餐厅.")

class IceCreamstand(Restaurant):
    def __init__(self,restaurant_name, restaurant_type):
        super().__init__(restaurant_name,restaurant_type)

        self.flavor = ['草莓', '苹果', '西瓜', '芒果', '奥利奥']

    def descriptive_flavor(self):
        print("口味:")
        for flavor in self.flavor:
            print(f"\t{flavor}")

my_ice  = IceCreamstand("乐事", "冰淇凌店")

my_ice.descriptive_flavor()