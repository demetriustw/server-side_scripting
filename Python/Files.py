# '/spam/eggs.png'

# print('\\')

# print(r'\\spam\\eggs.png')

# print('\\'.join(['folder1', 'folder2', 'folder3', 'folder4']))



import os

print(os.path.join('folder1', 'folder2', 'folder3', 'folder4'))

print(os.sep)

print(os.getcwd())

os.chdir('C:\\')
print(os.getcwd())

print('C:\\folder1\\folder2\\folder3\\spam.png')

print(os.chdir('C:\\xampp\\htdocs\\Python'))


print(os.path.abspath('spam.png'))

print(os.path.abspath('..\\..\\spam.png'))

print(os.path.isabs('c:\\folder\\folder'))

print(os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1'))

print(os.path.dirname('c:\\folder1\\folder2\\spam.png'))

print(os.path.basename('c:\\folder1\\folder2\\spam.png'))
print(os.path.basename('c:\\folder1\\folder2'))

print(os.path.exists('c:\\folder1\\folder2\\spam.png'))
print(os.path.exists('c:\\windows\\system32\\calc.exe'))

print(os.path.isfile('c:\\windows\\system32\\calc.exe'))
print(os.path.isfile('c:\\windows\\system32'))

print(os.path.isdir('c:\\windows\\system32\\calc.exe'))
print(os.path.isdir('c:\\windows\\system32'))

print(os.path.isdir('c:\\windows\\systasefaeveafdsf'))
print(os.path.isfile('c:\\windows\\systasefaeveafdsf'))

print(os.path.getsize('c:\\windows\\system32\\calc.exe'))
print(os.listdir('C:\\xampp\\htdocs\\Python'))


totalSize = 0

for filename in os.listdir('C:\\xampp\\htdocs\\Python'):
    if not os.path.isfile(os.path.join('C:\\xampp\\htdocs\\Python', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\xampp\\htdocs\\Python', filename))

print(totalSize)

# make delicious walnut waffles
# os.makedirs('c:\\delicious\\walnut\\waffles')

# helloFile = open('c:\\users\\z-wing\\hello.txt')
# content = helloFile.read()
# print(content)
# helloFile.close()

# helloFile = open('c:\\users\\z-wing\\hello.txt')
# print(helloFile.readlines())
# print(helloFile.close())

# helloFile = open('c:\\users\\z-wing\\hello2.txt', 'w')
# print(helloFile.write('Hello!!!!!!!'))
# print(helloFile.write('Hello!!!!!!!'))
# print(helloFile.write('Hello!!!!!!!'))
# print(helloFile.close())


baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()

print(os.getcwd())

# baconFile = open('bacon.txt', 'a')
# baconFile.write('\n\nBacon is delicious.')

# baconFile.close()


import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()


shelfFile = shelve.open('mydata')
shelfFile.keys()

print(list(shelfFile.keys()))
print(list(shelfFile.values()))
