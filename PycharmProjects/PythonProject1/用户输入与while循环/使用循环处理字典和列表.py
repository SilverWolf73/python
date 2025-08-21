#1.在列表之间移动
'''
new_users = ['silver wolf', 'golend sheep', 'kali root',]
users = []

while new_users:
    user = new_users.pop()
    print(f"欢迎{user.title()}加入")
    users.append(user)

print(f"用户数{len(users)}")
print(f"所有用户{users}")
'''
#3.删除特定值的元素
'''
pets = ['cat', 'dog', 'god', 'cat', 'wolf', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)
'''
#4.使用用户输入填充字典

informating = {}

print("------调查开始------")
start_1 = '请输入姓名： '
start_2 = '请输入年龄： '
start_3 = '请问是否继续（‘是’按1，‘否’按2）：'

judgment = True

while judgment:
    name = input(start_1)
    age = int(input(start_2))

    informating[name] = age

    judgment_1 = int(input(start_3))
    if judgment_1 == 2:
        judgment = False

print("------调查总结-----")
for name, age in informating.items():
    print(f"{name}:{age}")