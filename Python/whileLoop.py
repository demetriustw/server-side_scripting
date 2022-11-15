
spam = 0
while spam < 5:
    print('Hello world!')
    spam = spam + 1

name = ''
loop = -1
itteration = 0
while name != 'your name':
    if name == 'your name':
        break
    if loop == 1 and itteration < 1:
        print('Thats not your name.')
    if loop == 2 and itteration < 1:
        print('Come on just type your name.')
    if loop == 3 and name != 'fine' and itteration < 1:
        print('Why are you doing this. Just type your name!')
    if loop == 4 or name == 'fine' and loop == 3 or itteration == 1:
        if  name != 'fine':
            print('WHY! WHY MUST YOU FAIL ME SO OFTEN!')
            print('TYPE YOUR NAME!')
        elif name != 'YOUR NAME':
            print('NOOOOOOO!!!!')
        else:
            loop = -1
            itteration = itteration + 1
            print('Thank you, now')
    if loop == -1 or name == 'fine' and loop == 3:
        print('Please type your name.')
        loop = loop + 1
    loop = loop + 1
    name = input()
print('Thank you!')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))
