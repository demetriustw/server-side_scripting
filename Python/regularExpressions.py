# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False # not phone number-sized
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False # no area code
#     if text[3] != '-':
#         return False # missing dash
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False # no first 3 digits
#     if text[7] != '-':
#         return False #missing second dash
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False #missing last 4 digits
#     return True

# print(isPhoneNumber('hello'))

import re

#  foundNumber = False

# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
#         foundNumber = True
# if not foundNumber:
#     print('Could not find any phone numbers.')

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line')
print(mo.group())
print(phoneNumRegex.findall('Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line'))

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group())

print(mo.group(1))
print(mo.group(2))

phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
mo = phoneNumRegex.search('My number is (415) 555-4242')
print(mo.group())

batRegex = re.compile(r'Bat(man|mobile|copter|sie)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

mo = batRegex.search('Batmotercycle lost a wheel')
print(mo == None)

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo == None)

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())

mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo == None)

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo)
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo)




batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())


batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batman')
print(mo == None)
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())



regex = re.compile(r'\+\*\?')
print(regex.search('I learned about +*? regex syntax'))
regex = re.compile(r'(\+\*\?)+')
print(regex.search('I learned about +*?+*?+*?+*?+*?+*? regex syntax'))



haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('He said "HaHaHa"'))

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
print(phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000'))



haRegex = re.compile(r'(Ha){3,5}')
print(haRegex.search('He said "HaHaHa"'))
print(haRegex.search('He said "HaHaHaHaHa"'))
print(haRegex.search('He said "HaHaHaHaHaHaHa"'))


haRegex = re.compile(r'(Ha){3,}')


digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('1234567890'))

digitRegex = re.compile(r'(\d){3,5}?')
print(digitRegex.search('1234567890'))


phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex)

resume = 'sdoafneoaiefnoiaw508-555-5555aoeijfaoikenveoiasaeio508-555-1234'

print(phoneRegex.search(resume))

print(phoneRegex.findall(resume))

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(resume))

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume))




digitRegex = re.compile(r'\d')

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 gold rings, 4 calling birds, 3 french hens, 2 turtle doves and a partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))




vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food.'))

dubbleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(dubbleVowelRegex.findall('Robocop eats baby food.'))



consonantsRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantsRegex.findall('Robocop eats baby food.'))



beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('He said "Hello!"'))

endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))
print(endsWithWorldRegex.search('Hello world!aeafjkeabfvoejn'))



allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('039275893415718'))
print(allDigitsRegex.search('03927x893415718'))





atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))



atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))



print('First Name: Al Last Name: Sweigart')
print('First Name: Al Last Name: Sweigart'.find(':'))
print('First Name: Al Last Name: Sweigart'.find(':')+2)
print('First Name: Al Last Name: Sweigart'[12:])



nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Al Last Name: Sweigart'))



serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))


prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law'
print(prime)

dotStar = re.compile(r'.*')
print(dotStar.search(prime))
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))


vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))

vowelRegex = re.compile(r'[aeiou]', re.I)
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))


namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))



verboseNumb = re.compile(r'''
(\d\d\d-)|    # area code (without parens, with dash)
(\(\d\d\d-) ) # -or- area with parens and no dash
-         # first dash
\d\d\d    # first 3 digits
-         # second dash
\d\d\d\d  # last 4 digits
\sx\d{2,4}   # extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE) # (415) 555-5555, 415-555-5555

