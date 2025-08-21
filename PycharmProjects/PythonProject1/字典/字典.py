'''
student_ID = {'name' : '小明', 'age' : '15', 'ID' : '2025060112'}
print("name:", student_ID['name'])
print("age:", student_ID['age'])
print("ID:", student_ID['ID'])
'''
#1.创建空字典，添加键值对
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = '5'
print(alien_0)
#2.修改键值对

print(f"The alien is {alien_0['color']}, If klii alien have {alien_0['points']}")

alien_0['color'] = 'red'
alien_0['points'] = '10'
print(f"The alien is {alien_0['color']}, If klii alien have {alien_0['points']}")

#3.删除键值对

print(alien_0)

del alien_0['points']
print(alien_0)

#4.使用get()来访问值
print(alien_0.get('points', '无'))
