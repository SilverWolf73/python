#1.字典列表
'''
student_1 = {
    'name' : '李华',
    'class' : '6',
    'ID' : '20250060610'
}
student_2 = {
    'name' : '小明',
    'class' : '6',
    'ID' : '20250060611'
}
student_3 = {
    'name' : '小华',
    'class' : '6',
    'ID' : '20250060612'
}
students = [student_1, student_2, student_3]

for student in students:
    print(student)
'''
'''
aliens = []

for alien_namber in range(30):
    new_alien = {
        'color' : 'green',
        'points' : '5',
        'speen' : 'low',
    }
    aliens.append(new_alien)

print(f"一共建立{len(aliens)}个外星人。")

for alien in aliens[ :5]:
    print(alien)
'''
#2.在字典中存储列表
'''
favorite_OS = {
    'ben' : ['windows 11'],
    'jep' : ['ubuntu linux', 'kali linux'],
    'sam' : ['arch linux'],
    'lin' : ['fedora linux', 'manjora linux', 'deepin linux'],
}

for name, os in favorite_OS.items():
    print(f"{name.title()}喜欢的操作系统是:\n\t{os}")
'''
#3.在字典中存储字典
users = {
    '1000' : {
        'name' : 'silver wolf',
        'posts' : '舰长',
        'age' : '18',
    },
    '1001' : {
        'name' : 'golden sheep',
        'posts' : '副舰长',
        'age' : '17',
    },
}

for uid, information in users.items():
    print(f"UID:{uid}:")
    name = information['name'].title()
    posts = information['posts']

    print(f"\t姓名:{name}")
    print(f"\t职位:{posts}\n")