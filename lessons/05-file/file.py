# from sndhdr import tests
import random
from fileinput import filename
from lib2to3.fixes.fix_input import context

from sqlalchemy.testing.plugin.plugin_base import config

#filename = 'f1.txt'

# Запис
# with open(filename, 'w') as f:
#     f.write('New text')#

# Зчитування
# with open(filename, 'r') as f:
#     text = f.read()
#     print(text)

# f = open(filename, 'r')
# try:
#     text = f.read()
#     print(text)
# except FileExistsError:
#     print('End!')
# finally:
#     f.close()

# with open(filename, 'a') as file:
#     for n in range(0,10):
#         file.write(str(random.randint(-10,10)) + '\n')
#
# with open(filename, 'r') as file:
#     number = file.readline()
#     while number:
#         print(number)
#         number = file.readline()
# filename = 'f3.txt'
# with open(filename, 'w',encoding='utf-8') as file:
#     file.write('Text-utf-8.')
#
# with open(filename, 'r', encoding='utf-8') as file:
#         print(file.read())
filename = 'b1.txt'
with open(filename, 'ab') as file:
    file.write(b"\x4E\x4E\x4E\x4E\x2E")
with open(filename, 'rb') as file:
    content = file.readline()
    print(content)