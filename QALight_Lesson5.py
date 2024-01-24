# l = [1, 2, 3, 4, 5, 'Hello', True, 3.6, 'Hello World!', 'Hello World!!!!!!!']
# word = 'Hello'
# count = 0
# for elem in l:
#     if word == elem:
#         count = count + 1
# print(f"Count of world {word} : {count}")
#
#
#
#
# colors = ['red', 'green', 'blue']
# print(colors[0])
#
# colors.append('purple')
# print(colors)
# colors.insert(1, 'orange')
# print(colors)
#
#
# s = {7, 1, 2, 3, 4, 5, 6, 4, 3, 1, 8}
# print(s)
#
# l = 1, 2, 3, 4, 5, 3, 4, 1
# print(l)
# l1 = set(l)
# print(l1)
#
# l2 = frozenset(l)
# print(l2)
#
#
# # for k in d:
# #     print(k, d[k])
# #
# # print(d.items())
#
#
#
# colors = {(255, 0, 0): 'red', (0, 255, 0): 'green', (0, 0, 255): 'blue', (103, 78, 167): 'purple',
#           (212, 224, 54): 'mustard', 'red':(255, 0, 0), 'green': (0, 255, 0)}
#
# while True:
#     command = str(input("Enter command: [c], [r], [u], [d]"))
#     #Create
#     if command.lower() == 'c':
#         key = str(input("Enter color name: "))
#         value = str(input("Enter color value: "))
#         colors[key] = value
#
#     #Read
#     elif command.lower() == 'r':
#         for key, value in colors.items():
#             print(key, value)
#
#     #Update
#     elif command.lower() == 'u':
#         key = str(input("Enter color name: "))
#         new_value = str(input("Enter color value: "))
#         if key not in colors:
#             way = str(input("This key isn't present in colors. Do you want add it?: [y] or [n]: "))
#             if way == 'y':
#                 colors[key] = new_value
#         elif key in colors:
#             colors[key] = new_value
#
#
#     #Delete
#     elif command.lower() == 'd':
#         key = str(input("Enter color name: "))
#         result = colors.pop(key, "Not present")
#         print(f"Color {key} deleted with result {result}")


# #task_1
# first_number = int(input("Enter the first number: "))
# action = input("Enter the action [+], [-], [*], [/]: ")
# second_number = int(input("Enter the second number: "))
#
# if action == "+":
#     print(first_number+second_number)
# elif action == "-":
#     print(first_number - second_number)
# elif action == "*":
#     print(first_number * second_number)
# elif action == "/":
#     print(first_number / second_number)
# else:
#     print("Wrong number or action")



#tast_2
l = [23,45,2,80,40,-12,0,-2,49]
count_pos = 0
for elem in l:
    if elem > 0:
        count_pos += 1
print(count_pos)

count_neg = 0
for elem in l:
    if elem < 0:
        count_neg += 1
print(count_neg)

count_zero = 0
for elem in l:
    if elem == 0:
        count_zero += 1
print(count_zero)

#task_3.1
#3rd list includes all elements from 1st and 2nd lists:
l_1 = [11,12,13,14,15,16,0]
l_2 = [13,34,2,76,45,97,11]
l_1.extend(l_2)
print(l_1)

#task_3.2
#3rd list includes all unique elements from 1st and 2nd lists:
unique_elements = set(l_1)
print(unique_elements)

#task_3.3
#3rd list includes only the same elements form 1st and 2nd lists:
l_1 = [11,12,13,14,15,16,0]
l_2 = [13,34,2,76,45,97,11]
l_3 = []
for elem in l_1:
    if elem in l_2:
        l_3.append(elem)
print(l_3)

#task_3.4 (as for me the conditions are the same like in 3.2, maybe I undertood incorrectly )
#3rd list includes all unique elements from each list (1st and 2nd):
l_1 = [1,2,2,3]
l_2 = [7,3,4,5,5]
l_1.extend(l_2)
unique_elements = set(l_1)
print(unique_elements)

#task_3.5
#3rd list includes min and max elements from each list:
l_1 = [1,2,3,4]
l_2 = [5,6,7,8]
l_1.sort()
min_val_list_1 = l_1[0]
max_val_list_1 = max(l_1)
l_2.sort()
min_val_list_2 = l_2[0]
max_val_list_2 = max(l_2)

l_3=[min_val_list_1,max_val_list_1,min_val_list_2,max_val_list_2]
print(l_3)



#task_4
#Add a new tuple and print it:
my_tup = (3,'one', 5)
print(my_tup)

#Add a new tiple and change one element of the tuple:
# How I know we can't change the elements of tuple,
# but it possible if we change tuple to list,
# update element and return it to the tuple
my_tup = (3,'one', 5)
l = list(my_tup)
l[0] = '4'
my_tup=tuple(l)
print(my_tup)



#task_5
# #5.1 Add new item
item = {'name': 'pencil', 'price': 2, 'quantity': 10}
item['name1'] = 'pen'
item['price1'] = 5
item['quantity1'] = 25
print(item)

#5.2 Search and print
books = {
    "Lessons in Chemistry": {
        "author": "Bonnie Garmus",
        "year": "2022"
    },
    "The Lincoln Highway": {
        "author": "Amor Towles",
        "year": "2023"
    },
    "People We Meet on Vacation": {
        "author": "Emily Henry",
        "year": "2021"
    }
}
print(books["The Lincoln Highway"])

#5.3 Remove item
students = {"Bonnie Garmus": 200, "Amor Towles": 180, "Emily Henry": 195}
rem = students.pop("Bonnie Garmus", "200")
print(students)

#task_6.1:
s_1 = {1,2,3,4,5,6,7,8,9}
s_2 = {2,33,4,54,7,9,8}
union_s1_with_s2 = s_1.union(s_2)
print(union_s1_with_s2)

inters = s_1.intersection(s_2)
print(inters)

differ1 = s_1.difference(s_2)
differ2 = s_2.difference(s_1)
print(differ1, differ2)
#or using the symmetric_difference
sym_differ = s_1.symmetric_difference(s_2)
print(sym_differ)

#task_6.2 (If I understood the task correctly, if the sets aren't equel it's true (more or less)):
s_1 = {1,2,3,4,5}
s_2 = {1,2,3,4,5,6}
if s_2 > s_1 or s_2 < s_1:
    print(True)
else:
    print(False)

#task_6.3:
s_1 = set('qwertyui')
s_2 = set('asdeqgy')

union_s1_with_s2 = s_1.union(s_2)
print(union_s1_with_s2)

inters = s_1.intersection(s_2)
print(inters)

differ1 = s_1.difference(s_2)
differ2 = s_2.difference(s_1)
print(differ1, differ2)
#or using the symmetric_difference
sym_differ = s_1.symmetric_difference(s_2)
print(sym_differ)

#task_6_4 Add and remove elements:
s = {"one", "two", "three"}
s.add("four")
s.remove("one")
print(s)