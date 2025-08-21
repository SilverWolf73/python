#1.使用input函数
'''
name =  input("请输入姓名: ")
print(f"你好，{name}")
'''
#2.使用int来获取数值
age = int(input("你的年龄是: "))
if age < 18 :
    print(f"你才{age}，你还没有成年.")
elif age < 35 :
    print("成年人")
