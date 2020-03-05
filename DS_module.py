from math import sqrt
print("Square root of 16 is", sqrt(16))

import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

import DS_name_in_module as nim
# from DS_name_in_module import say_hi,__version__
# from DS_name_in_module import *
nim.say_hi()
print('Version', nim.__version__)

