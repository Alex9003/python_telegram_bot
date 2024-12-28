# print("number 1:")
# n1 = int(input())
# print("number 2:")
# n2 = int(input())
#
#
# try:
#     d = n1 / n2
#     print(d)
# except ZeroDivisionError:
#     print('Error: division by 0')
# else:
#     print('Else!')
# finally:
#     print('Finally')
#
# print('End')

# Приклад 2 -------------------------
# f = None
# try:
#     with open('f1.txt') as file:
#         f = file.read()
# except FileNotFoundError:
#     with open('f1.txt', 'w') as file:
#         file.write('something')
# finally:
#     if not f:
#         with open('f1.txt') as file:
#             f = file.read()
#
# print(f)

class FifeDivisionError(Exception):
    def __init__(self, mesage, error_code):
        super().__init__(mesage)
        self.error_code = error_code

def divide_number(a, b):
    if 5 == b:
        raise  FifeDivisionError('Dividion by 5 can\'t',2024)
    return a/b

try:
    d = divide_number(12,5)
    print(d)
except FifeDivisionError as error:
    print(f'Error {error}')
    print(f'Code error: {error.error_code}')