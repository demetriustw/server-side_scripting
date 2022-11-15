# '/spam/eggs.png'
print('//')

print(r'/spam/eggs.png')

print('//'.join(['folder1', 'folder2', 'folder3', 'folder4']))



import os

print(os.path.join('folder1', 'folder2', 'folder3', 'folder4'))

print(os.sep)

print(os.getcwd())

os.chdir('//')
print(os.getcwd())

print('//folder1//folder2//folder3//spam.png')

os.chdir('/Applications/XAMPP/xamppfiles/htdocs')


print(os.path.abspath('spam.png'))

print(os.path.abspath('..//..//spam.png'))

print(os.path.isabs())