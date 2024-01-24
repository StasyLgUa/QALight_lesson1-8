#files
#Create
# f = open("text1.txt", "wt")
# f.write("Hello World!\n")
# f.write("My name is Anastasiia_updated")
#
# f.close()

#Read
# f = open("text1.txt", "rt")
# a = f.read()
# print(a)
# f.close()

#Append
# f = open("text1.txt", "at")
# f = f.write("Run test\n")
# f = f.write("First test\n")
# f.close()

# import random
# f = open("text2.txt", "wt")
# for i in range(200):
#     a = str(random.randint(100,999))
#     f.write(a)
#     f.write("\n")
# f.close()
#
# #Вывести простые числа
# calc = open("text2.txt", "rt")
# l = calc.readlines()
# for line in l:
#     flag = True
#     for i in range(2, int(line[:-1])):
#         if int(line[:-1]) % i == 0:
#             flag = False
#     if flag:
#         print(line[:-1])
# calc.close()
#
# #Вывести числа по возрастанию
# calc = open("text2.txt", "rt")
# l = calc.readlines()
# l.sort()
# for line in l:
#     print(line[:-1])
# calc.close()
#
# #Вывести уникальные числа
# calc = open("text2.txt", "rt")
# l = calc.readlines()
# l = set(l)
# l = list (l)
# l.sort()
# for line in l:
#     print(line[:-1])
# calc.close()
#
#
# book = open("example.html", "rt")
# a = book.readlines()
# for line in a:
#     if 'HREF="http' in line:
#         b = line[line.find("http"):line.find('" ADD_DATE')]
#         print(b)
# book.close()


#-----------
#Task_1
import random
f_1 = open("test_file_01", "wt")
for i in range(50):
    a = str(random.randint(10,30))
    f_1.write(a)
    f_1.write("\n")
f_1.close()

f_2 = open("test_file_02", "wt")
for i in range(50):
    a= str(random.randint(10,30))
    f_2.write(a)
    f_2.write("\n")
f_2.close()
from itertools import zip_longest
with open("test_file_01") as f_1, open("test_file_02") as f_2:

    for a, b in zip_longest(f_1, f_2):
        if a != b:
            print("Not equal digits: " + a + b)


#Task_2
f_1 = open("test_file_01", "rt")
l = f_1.readlines()
vowels = "aeuioy"
consonants = "qwrtpsdfghjklzxcvbnm"
dig = 0
qv = 0
qc = 0
for r in l:
    for b in r:
        if b in vowels:
            qv += 1
        elif b in consonants:
            qc += 1
        elif b.isdigit():
            b = int(b)
            dig +=1
f_2 = open("test_file_with_results", "wt")
f_2.write("Quantity of vowels is ")
f_2.write(str(qv))
f_2.write("\nQuantity of rows is ")
f_2.write(str(len(l)))
f_2.write("\nQuantity of consonants is ")
f_2.write(str(qc))
f_2.write("\nQuantity of digits is ")
f_2.write(str(dig))
f_2.write("\nQuantity of all symbols is ")
f_2.write(str(qv+qc+dig))

f_1.close()
f_2.close()

#Task_3
f_1 = open("test_file_01", "rt")
l = f_1.readlines()
l = list(l)
rem_line = l.pop()
l_up = str(l)
f_2 = open("file_after_remove_last_line.txt", "wt")
f_2.write(l_up)
f_1.close()
f_2.close()

#Task_4
f_1 = open("test_file_01", "rt")
l = f_1.readlines()
l = list(l)
q=0
for r in l:
    w = len(r)-1
    q =+1
longest_row = max(l, key=len)
print(len(longest_row))





