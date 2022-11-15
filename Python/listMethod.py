spam = ['hello', 'hi', 'howdy', 'heyas']

print(spam.index('hello'))

print(spam.index('heyas'))

# print(spam.index('asdfeaw'))

spam = ['Sophie', 'Pooka', 'Fat-tail', 'Pooka']

print(spam.index('Pooka'))

spam = ['cat', 'dog', 'bat']

spam.append('moose')
print(spam)

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)

spam.append('moose')
spam.append('moose')
spam.append('moose')
spam.append('moose')

print(spam)


eggs = 'hello'

# eggs.append('world')

spam = ['cat', 'bat', 'rat', 'elephant']

spam.remove('bat')
print(spam)
# spam.remove('bat')

del spam[0]
print(spam)

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
print(spam)

spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

spam = [1,2,3, 'Alice', 'Bob']
# spam.sort()
print(spam)

spam = ['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

spam = ['a','z','A','Z']
spam.sort()
print(spam)

spam.sort(key=str.lower)
print(spam)