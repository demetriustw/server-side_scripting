# raise Exception('This is the error message.')

# """

# **************
# *            *
# *            *
# *            *
# **************

# """

# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('"symbol" needs to be a string of length 1.')
#     if (width < 2) or (height < 2):
#         raise Exception('"width" and "height" must be grater or equal to 2.')
#     print(symbol * width)

#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)

#     print(symbol * width)

# boxPrint('*', 2, 2)
# boxPrint('()', 5, 16)

import traceback
# try:
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('error_log.txt', 'a')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written error_log.txt')


# assert False, 'This is the errror message.'

# market_2nd = {'ns': 'green', 'ew': 'red'}

# def switchLights(intersection):
#     for key in intersection.keys():
#         if intersection[key] == 'green':
#             intersection[key] = 'yello'
#         elif intersection[key] == 'yello':
#             intersection[key] = 'red'
#         elif intersection[key] == 'red':
#             intersection[key] = 'green'
#     assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

# print(market_2nd)
# switchLights(market_2nd)
# print(market_2nd)

import logging

logging.basicConfig(filename='.\Python\\myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

# print(1*2*3*4)
# print(1*2*3*4*5*6*7)

logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('end of program')
