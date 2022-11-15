import random
from random import *

spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[randint(0,3)])

spam = [['cat', 'bat'], [10,20,30,40,50]]

if spam[randint(0, 1)] == spam[0]:
    print(spam[0][randint(0,1)])
else:
    print(spam[1][randint(0,4)])
    

spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[randint(-3,0)])

print('The ' + spam[-1] + ' is afraid of the ' + spam[-2] + '.')

print(spam[1:3])

spam = 'Hello'
print(spam)

spam = [10, 20, 30]
spam[1] = 'Hello'
print(spam)
spam[1:3] = ['CAT','DOG','MOUSE']
print(spam)

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2])

print(spam[1:])

spam = ['cat', 'bat', 'rat', 'elephant']

del spam[2]
print(spam)

del spam[2]
print(spam)


print(len('Hello'))

print(len([1,2,3]))

print('Hello ' + 'world')

print([1,2,3] + [4,5,6])

print('Hello' * 3)

print([1,2,3] * 3)

print(int('42'))

print(str(42))

print(list('Hello'))

print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])

print(42  in ['hello', 'hi', 'howdy', 'heyas'])

print('howdy' not in ['hello', 'hi', 'howdy', 'heyas'])
