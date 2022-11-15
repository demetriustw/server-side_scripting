# def hello(name):
#     print('Hello ' + name)

# hello('Alice')
# hello('Bob')

# print('Hello has ' + str(len('hello')) + ' letters in it.')

# def plusOne(number):
#     return number + 1

# newNumber = plusOne(5)
# print(newNumber)

# print('Hello', end=' ')
# print('World')


# a='Hello'
# b='World'

# print(a * 5 ,b * 5 , sep=' ')

# global and local scope

# spam = 42 # global variable

# def eggs():
#     spam = 42 # local variable

# print('Some code here.')
# print('Some more code.')

# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0

# spam()

# def spam():
#     # always looks for global var eggs
#     # renaming eggs to 'Hello'
#     global eggs
#     eggs = 'Hello'
#     # only if no local var in spam
#     # prints eggs global
#     print(eggs)

# eggs = 42
# spam()
# print(eggs)