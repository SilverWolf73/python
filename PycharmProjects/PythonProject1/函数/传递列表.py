#0.展示
'''
def greeing(names):
    for name in names:
        print(f"你好{name}")

names = ['Silver', 'kali', 'root']

greeing(names=names)
'''
#1.在函数中修改列表
'''
def print_models(preparation_print, complete_print):
    while preparation_print:
        complete_print.append(preparation_print.pop())

def show_models(complete_print):
    for models in complete_print:
        print(f"打印完成{models.title()}")

preoaration_print = ['模型飞机', '模型机甲', '模型坦克']
complete_print = []

print_models(preoaration_print, complete_print)
show_models(complete_print=complete_print)
'''
#2.禁止函数修改列表
def print_models(preparation_print, complete_print):
    while preparation_print:
        complete_print.append(preparation_print.pop())

def show_models(complete_print):
    for models in complete_print:
        print(f"打印完成{models.title()}")

preoaration_print = ['模型飞机', '模型机甲', '模型坦克']
complete_print = []

print_models(preoaration_print[:], complete_print)
show_models(complete_print=complete_print)
print(preoaration_print)
print(complete_print)

