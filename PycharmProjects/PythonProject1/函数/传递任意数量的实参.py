#0.展示
'''
def print_name(*name):
    #*name创建元组
    print(name)

print_name("Silver")

print_name("kali","root")
'''


#1.位置实参结合任意数量的实参
'''
def make_pizza(size, *toppings):
    print(f"制作一个{size}寸加小料:")
    for topping in toppings:
        print(f"\t{topping}")

make_pizza(12, '芝士', '牛肉')
'''
#2.使用任意数量的关键字实参
def survey(name,power,**information):
    information['姓名'] = name
    information['势力'] = power
    return information

informations = survey("华", "仙舟", 年龄 = 5000, 命途 = "巡猎")

print(informations)