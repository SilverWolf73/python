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

restaurant = Restaurant("冰清", "雪糕店")

restaurant.open_restaurant(12)

restaurant.introduse()

restaurant.shut_restaurant(18)