#1.位置实参
'''
def survey(name,posts):
    print(f"你好{name.title()},你的职位是{posts}")
    print("欢迎入职本公司\n")

survey('临夏', '经理')
survey('霞缘', '主管')
'''

#2.关键字实参
'''
def survey(name,power):
    print(f"姓名：{name.title()},所处势力：{power.upper()}")

survey(name='华', power='仙舟')
survey(power='仙舟',name='华')
'''
#3.默认值
'''
def survey(name,power='公司'):
    print(f"姓名：{name.title()},所处势力：{power.upper()}")

survey(name='砂金')

survey(name='华',power='仙舟')
'''