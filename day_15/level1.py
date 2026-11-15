# # Python Type Errors
# PS D:\dev\30DaysOfPython\day_15> python
# Python 3.15.1 (tags/v3.15.1:c37e74c, Oct 21 2026, 06:24:08) [MSC v.1951 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL (https://aka.ms/python-native-repl)
# >>> print 'hello word'
#   File "<python-input-0>", line 1
#     print 'hello word'
#     ^^^^^^^^^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# >>> print('hello world')
# hello world
# >>> print(age)
# Traceback (most recent call last):
#   File "<python-input-2>", line 1, in <module>
#     print(age)
#           ^^^
# NameError: name 'age' is not defined
# >>> age = 25
# >>> print(age)
# 25
# >>> numbers = [2, 3, 4, 5]
# >>> numbers[5]
# Traceback (most recent call last):
#   File "<python-input-6>", line 1, in <module>
#     numbers[5]
#     ~~~~~~~^^^
# IndexError: list index out of range
# >>> import maths
# Traceback (most recent call last):
#   File "<python-input-7>", line 1, in <module>
#     import maths
# ModuleNotFoundError: No module named 'maths'
# >>> import math
# >>> math.PI
# Traceback (most recent call last):
#   File "<python-input-9>", line 1, in <module>
#     math.PI
# AttributeError: module 'math' has no attribute 'PI'. Did you mean '.pi' instead of '.PI'?
# >>> math.pi
# 3.141592653589793
# >>> users = {'name': 'Asab', 'age': 250, 'country': 'Finland'}
# >>> users['name]
#   File "<python-input-12>", line 1
#     users['name]
#           ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> users['name']
# 'Asab'
# >>> users['ocure']
# Traceback (most recent call last):
#   File "<python-input-14>", line 1, in <module>
#     users['ocure']
#     ~~~~~^^^^^^^^^
# KeyError: 'ocure'
# >>> user['country']
# Traceback (most recent call last):
#   File "<python-input-15>", line 1, in <module>
#     user['country']
#     ^^^^
# NameError: name 'user' is not defined. Did you mean: 'users'?
# >>> users['country']
# 'Finland'
# >>> 4 + '3'
# Traceback (most recent call last):
#   File "<python-input-17>", line 1, in <module>
#     4 + '3'
#     ~~^~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>> from math import power
# Traceback (most recent call last):
#   File "<python-input-18>", line 1, in <module>
#     from math import power
# ImportError: cannot import name 'power' from 'math' (unknown location)
# >>> from math import pow
# >>> pow(2, 5)
# 32.0
# >>> int('12s')
# Traceback (most recent call last):
#   File "<python-input-21>", line 1, in <module>
#     int('12s')
#     ~~~^^^^^^^
# ValueError: invalid literal for int() with base 10: '12s'
# >>> 1/0
# Traceback (most recent call last):
#   File "<python-input-22>", line 1, in <module>
#     1/0
#     ~^~
# ZeroDivisionError: division by zero