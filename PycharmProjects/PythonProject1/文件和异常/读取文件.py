#1.读取文件全部内容
#2.相对路径和绝对路径
'''
from pathlib import Path

path = Path('/home/SilverWolf/pi.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)
'''
#3.访问文件中的各行
'''
from pathlib import Path

path = Path('/home/SilverWolf/pi.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()
for line in lines:
    print(line)
'''
#4.使用文件力度能容
'''
from pathlib import Path

path = Path('/home/SilverWolf/pi.txt')
contents = path.read_text().rstrip()
ip_string = ''

lines = contents.splitlines()
for line in lines:
    ip_string += line.lstrip()

print(ip_string)
print(len(ip_string))
'''
#5.包含100位的大型文件
'''
from pathlib import Path

path = Path('/home/SilverWolf/pi_million.txt')
contents = path.read_text().rstrip()
pi_string = ''

lines = contents
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
'''
from pathlib import Path
path = Path('/home/SilverWolf/pi_million.txt')

contents = path.read_text().rstrip()
pi_string = ''

lines = contents
for line in lines:
    pi_string += line.lstrip()

brithday = input("请输入你的生日: ")

if brithday in pi_string:
    print('yes')
else:
    print('no')