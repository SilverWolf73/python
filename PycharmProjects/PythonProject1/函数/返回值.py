#1.可选实参
'''
def survey(name, power, topf=''):
    if topf:
        information = f"姓名：{name.title()}\n势力：{power.upper()}\n命途：{topf.upper()}"
    else :
        information = f"姓名：{name.title()}\n势力：{power.upper()}"
    return information

print(survey(name='华',power='仙舟',topf='巡猎'))

print(survey(name='星',power='星穹列车'))
'''


#2.返回字典

informations = []

def survey(name, age, sex=None):
    information = {
        '姓名' : name,
        '性别' : sex,
        '年龄' : age,
    }
    return information

start_1 = '输入姓名： '
start_2 = '输入性别(可不添）: '
start_3 = '输入年龄： '
judgment = True
while judgment:
    name = input(start_1)
    if name == 'q':
        break
    sex = input(start_2)
    if sex == 'q':
        break
    age = int(input(start_3))
    if age == 'q':
        break
    informations.append(survey(name=name, age=age, sex=sex))

print(informations)