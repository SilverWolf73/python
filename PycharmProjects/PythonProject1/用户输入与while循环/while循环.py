#1.使用while循环
'''
num = 1
while num <=5:
    print(num)
    num += 1
'''
#2.使用标志
'''
start = "请输入一段话："

active = True

while active:
    message = input(start)

    if message == 'quit':
        active = False
    else :
        print(message)
'''
#3.break退出
'''
start = "请输入你喜欢的语言："

while True:
    language = input(start)

    if language == 'quit':
        break
    else :
        print(f"你喜欢{language.title()}语言")
'''
#4.循环使用continue
#打印1～10的奇数
num = 0

while num < 10 :
    num += 1
    if num % 2 == 0:
        continue
    print(num)
