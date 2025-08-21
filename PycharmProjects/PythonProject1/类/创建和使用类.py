class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        #模拟小狗坐下
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        #模拟小狗打滚
        print(f"{self.name} rolled over")

'''在类中函数称为方法'''

my_dog = Dog('无', 6)

#通过self.name获取属性
print(f"我的狗名字是{my_dog.name}")
print(f"我的狗{my_dog.age}岁了")

my_dog.sit()
my_dog.roll_over()