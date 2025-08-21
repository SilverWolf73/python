#1.导入整个模块
'''
import 用户信息

information = 用户信息.survey("琪亚娜", '17', 网名 = "叱咤月海鱼猫猫",UID = 1000)

print(information)
'''
#2.导入特定函数
'''
from 用户信息 import survey

information = survey("琪亚娜", '17', 网名 = "叱咤月海鱼猫猫",UID = 1000)

print(information)
'''
#3.使用as给函数指定别名
'''
from 用户信息 import survey as su

information = su("琪亚娜", '17', 网名 = "叱咤月海鱼猫猫",UID = 1000)

print(information)
'''
#4.使用as给模块指定别名
'''
import 用户信息 as user

information = user.survey("琪亚娜", '17', 网名 = "叱咤月海鱼猫猫",UID = 1000)

print(information)
'''
#5.导入模块中所有函数
'''
from 用户信息 import *

information = survey("琪亚娜", '17', 网名 = "叱咤月海鱼猫猫",UID = 1000)

print(information)
'''