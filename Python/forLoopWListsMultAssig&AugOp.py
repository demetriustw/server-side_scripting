for i in range(4):
    print(i)

print(range(4))

for i in [0, 1, 2, 3]:
    print(i)

print(list(range(4)))

spam = list(range(0, 100, 2))

print(spam)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
    j = i + 1
    print('Index ' + str(j) + ' in supplies is: ' + supplies[i])

# supplies = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens']

# for i in range(len(supplies)):
#     j = i + 1
#     print('Index ' + str(j) + ' in supplies is: ' + supplies[i])


cat = ['fat', 'orange', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

size, color, disposition = cat
print(size)
print(color)

size, color, disposition = 'skinny', 'black', 'quiet'

a = 'AAA'
b = 'BBB'

a, b = b, a

print(a)
print(b)

spam = 42
spam = spam + 1
spam += 1
print(spam)