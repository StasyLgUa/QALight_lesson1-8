# import random
#
# f = open("test1.txt", "wt")
# for i in range(200):
#     f.write(str(random.randint(100, 999)))
#     f.write('\n')
# f.close()
#
# test = open("test1.txt", "rt")
#
# word = test.readline()
#
# while word:
#     # Корисне навантаження
#     print(word)
#     word = test.readline()
#
# test.close()
#1
import random
# test = open("test1.txt", "rt")
# odd = open("odd.txt", "wt")
# even = open("even.txt", "wt")
#
# word = test.readline()
#
# while word:
#     letters = word[:-1]
#     number = int(letters)
#     if number % 2 == 0:
#         even.write(word)
#     elif number % 2 != 0:
#         even.write(word)
#
#     word = test.readline()
#
# odd.close()
# even.close()
# test.close()
#
#
# #2
# test = open("test1.txt", "rt")
# odd = open("odd.txt", "wt")
# even = open("even.txt", "wt")
#
# word = test.readline()
#
# while word:
#     try:
#         letters = word[:-1]
#         number = int(letters)
#         if number % 2 == 0:
#             even.write(word)
#         elif number % 2 != 0:
#             even.write(word)
#     except:
#         continue
#     finally:
#         word = test.readline()
#
# odd.close()
# even.close()
# test.close()

#-------------json
# import json
# #Сериализация
# notes = {'a': 1, 'b': 2, 'c': 3, 'd': {'e':4, 'f': 5, 'g': 6}}
# print(json.dumps(notes, sort_keys=True, indent=4))
# with open("something.json", 'wt') as file:
#     json.dump(notes, file)
#
# #Десериализация
# a = json.dumps(notes, sort_keys=True, indent=4)
# d_a = json.loads(a)
# print(d_a["d"]["f"])
# print(d_a)
#
# with open("something.json", 'rt') as file:
#     d_q = json.load(file)
# print(d_q)

# Объявление функции

# def some_file(name = 'test0', lenght=200):
#     import random
#     f = open(f"{name}.txt", "wt")
#     for i in range(lenght):
#         f.write(str(random.randint(100, 999)))
#         f.write('\n')
#     f.close()
# #Вызов функции
# some_file()
# some_file('test10', 400)

# def some_file(name="test1"):
#     f = open(f"{name}.txt", "rt")
#     print(f.read())
#     f.close()
#
# some_file("test0")
# def print_data(name):
#     f= open(f"{name}.txt", "rt")
#     print(f.read())
#     f.close()
#
# print_data("test01")
#
# # Порядок атрибутов\ Упрядочивание
# def something(a, b, c=3, d=5, *e, **f): # a, b - упорядоченные атрибуты
#     #c, d - атрибуты по умолчанию. e args = неупорядоченные атрибуты
#     return a,b,c,d,e,f
# print(something(10, 5, 15, 25, 3, 5, 6, 7, "Hello", "Good", lenght=1, direction='horizontal'))
#

#task_1
def text(*e):
    print('''
“Don't let the noise of others'
    opinions drown out your
            own inner voice.
                Steve Jobs"
''')
text()

#task_2
def symb(a,b):
    i=0
    for i in range(a,b):
        if i%2 != 0:
            print(i)
            i = +1

symb(10,30)


#task_3
def lines(len, symb, location):
    line = symb*len
    if location == 'r':
        r_l = line.rjust(len)
        print(r_l)
    elif location == 'l':
        l_l = line.ljust(len)
        print(l_l)
    return

lines(50,'-', 'l')

#task_4
def max_digit(a,b,c,d):
    print(max(a,b,c,d))

max_digit(1,32,55,23)

#task_5
def summ_of_digits(a,b):
    print (sum(range(a,b)))

summ_of_digits(1,5)

#task_6:
def check_is_prime_number(a):
    num = a
    c = 0
    for i in range(1, num+1):
        if num%i==0:
            c = c + 1
    if c == 2:
        print(True)
    else:
        print(False)


check_is_prime_number(7)

#task_7
def happy_number(a):
    num = str(a)
    first_part = int(num[0]) + int(num[1]) + int(num[2])
    second_part = int(num[3]) + int(num[4]) + int(num[5])
    if first_part == second_part:
        print(True)
    else:
        print(False)

happy_number(123420)


'''
Завдання 1:
Напишіть функцію, яка виводить на екран відформатований текст, зазначений нижче:
“Don't let the noise of others' 
    opinions drown out your 
            own inner voice.”
                    Steve Jobs
'''


