#1.遍历所有的键值对
users = {
    'user_name_1' : 'Silver Wolf' ,
    'user_name_2' : 'Golden Sheep' ,
    'user_name_3' : 'Kali Root',
    'user_name_4' : 'Code Lin'
}
IDs = ['user_name_1', 'user_name_2']
'''
for user_ID, user_name in users.items():
    print(f"\n欢迎回来,用户{user_name}")
'''
#2.遍历字典上的所用键
'''
for user_ID in users.keys():
    print(user_ID)
'''
'''
for ID in users.keys():
    print(f"Hi,{users[ID]}")

    if ID in IDs:
       print("欢迎回来,舰长")
'''
#3.按顺序遍历字典
#4.遍历字典的所有值
for user_name in users.values():
    print(f"欢迎回来,{user_name.title()}")
    