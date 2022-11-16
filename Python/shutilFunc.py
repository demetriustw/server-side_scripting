import shutil

# shutil.copy('C:\\Users\\z-wing\\spam.txt', 'C:\\Users\\z-wing\\delicious')

# shutil.copy('C:\\Users\\z-wing\\spam.txt', 'c:\\delicious\\spamspamspam.txt')

# shutil.copytree('C:\\Users\\z-wing\\delicious', 'C:\\Users\\z-wing\\delicious_backup')

# shutil.move('C:\\Users\\z-wing\\spam.txt', 'C:\\Users\\z-wing\\delicious\\walnut')
# shutil.move('C:\\Users\\z-wing\\delicious\\walnut\\spam.txt', 'C:\\Users\\z-wing\\delicious\\walnut\\eggs.txt')

import os
# delete empty files
# os.unlink('bacon.txt')

# delete empty files
# os.rmdir('c:\\Users\\z-wing\\delicious')

# delete ALL files
# shutil.rmtree('c:\\Users\\z-wing\\delicious')

# os.chdir('c:\\Users\\z-wing\\Desktop')

# for filename in os.listdir():
#     if filename.endswith('.txt'):
        # os.unlink(filename)
        # print(filename)

import send2trash
# send2trash.send2trash('c:\\Users\\z-wing\\Desktop\\New folder')

for folderName, subfolders, filenames in os.walk('c:\\delicious'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders)) 
    print('The filenames in ' + folderName + ' are: ' + str(filenames)) 
    print()

    for subfolder in subfolders:
        # print(subfolder)
        # os.unlink(subfolder)
        if 'fish' in subfolder:
            # os.rmdir(subfolder)
            print('rmdir on '+ subfolder)
    
    for file in filenames:
        if file.endswith('.py'):
            # shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))
            print('renaming on '+ folderName)