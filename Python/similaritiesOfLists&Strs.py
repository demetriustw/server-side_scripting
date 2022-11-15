print(list('Hello'))

name = 'Zophie'
print(name[0])

print(name[1:3])

print(name[-2])

print('Zo' in name)

print('xxx' in name)

for letter in name:
    print(letter)

name = 'Zophie the cat'
print(name[7])
# name[7] = 'x'
# print(name[7])

name = 'Zophie a cat'
newName = name[:7] + 'the' + name[8:]
print(newName)

spam = 42
cheese = spam
spam = 100

print(cheese)
print(spam)

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(cheese)
print(spam)

def eggs(cheese):
    cheese.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)

import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42

print(cheese)
print(spam)


spam = ['apples',
        'oranges',
        'bananas',
        'cats']

print('Four score and seven ' + \
       'years ago')

print('Four score and seven ' + 'years ago')
