from random import randint, choice

i = 5

while i:
    print(randint(1, 6))
    i -= 1

plan = ['j-20', 'j-35', 'j-16']

while i < 5:
    print(choice(plan))
    i += 1