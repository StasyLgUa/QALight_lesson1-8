# age = 18
# gender = "male"  # "female"
#
# if age < 18:
#     print("You are a child")
# else:
#     print("You are an adult")
#
# print(5 > 3)
# print(5 < 3)
# print(5 >= 5)
# print(5 <= 5)
# print(4 == 5)
# print(4 != 3)
#
# height = 119
# if height < 120:
#     print("Forrbiden")
# elif height < 140:
#     print("Allowed with conditions")
# else:
#     print("Allowed")
#
#

#
# a=0
# while a<10:
#     print(a)
#     a=a+1
#
# a=1
# b=36
# while a <= b:
#     if a % 2 !=0:
#         print(a) #odd
#     a = a + 1
#
#
# for i in 1, 2, 3, 4, 5, 6, 7, 8, 9:
#     print(i)
#
# print("--------------------")
# a=1
# b=36
# for i in range(a, b+1):
#     if i % 2 !=0:
#         print(i) #odd
#
#
# a=1
# b=36
# while a <= b:
#     if a % 2 ==0:
#         print(a) #odd
#     a = a + 1

# a=1
# b=36
# while a<=b:
#     print(a+(a+1))
#     a=a+1

# a=1
# b=36
# summa = 0
# for i in range(a,b + 1):
#     summa = summa + i
# print(summa)
#
# #каждый 5й элемент:
# a=1
# b=36
# summa = 0
# while a <= b:
#     if a%5 == 0:
#         print(a)
#         #break
#     a=a+1


# a = 1
# b = 36
# summa = 0
# for i in range (0, 37):
#     summa = summa + 1
#     print(i)


#task_1
# a=int(input("Enter number 1: "))
# b=int(input("Enter number 2: "))
# c=int(input("Enter number 3: "))
# decision=int(input("What would you like to do? If you want to sum up please enter '1' or if you want to multiply please enter '0': "))
# if decision == 1:
#     summa_of_numbers = int(a+b+c)
#     print(summa_of_numbers)
# elif decision == 0:
#     multiply_of_numbers = int(a*b*c)
#     print(multiply_of_numbers)
# else:
#     print("Wrong number")


#task_2
# a=int(input("Enter number 1: "))
# b=int(input("Enter number 2: "))
# c=int(input("Enter number 3: "))
# decision=int(input("What would you like to do? If you want to see the maximum value please enter '1' or if you want to see the minimum value please enter '0' or if you want to see the arithmetical mean value please enter '2': "))
# if decision == 1:
#     print(max(a,b,c))
# elif decision == 0:
#     print(min(a,b,c))
# elif decision == 2:
#     average = float((a+b+c)/3)
#     print(average)
# else:
#     print("Wrong number")


#task_3
# day=int(input("Please enter any number from 1 to 7 (including)"))
# if day == 1:
#     print("Monday")
# elif day ==2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Wrong number")

#task_4
# year=int(input("Please enter any number from 1 to 12 (including)"))
# if year == 1:
#     print("January")
# elif year ==2:
#     print("February")
# elif year == 3:
#     print("March")
# elif year == 4:
#     print("April")
# elif year == 5:
#     print("May")
# elif year == 6:
#     print("June")
# elif year == 7:
#     print("July")
# elif year == 8:
#     print("August")
# elif year == 9:
#     print("September")
# elif year == 10:
#     print("October")
# elif year == 11:
#     print("November")
# elif year == 12:
#     print("December")
# else:
#     print("Wrong number")


#task_5
# value = int(input("Enter any number: "))
# if value > 0:
#     print("Number is positive")
# elif value < 0:
#     print("Number is negative")
# elif value == 0:
#     print("Number is equal to zero")


#task_6
# value_1 = int(input("Enter any number: "))
# value_2 = int(input("Enter any number: "))
# if value_1 != value_2:
#     if value_1 > value_2:
#         print(value_2, value_1)
#     else:
#         print(value_1, value_2)
# else:
#     print(f"Value {value_1} is equal to value {value_2}")

#task_7
# val_1 = int(input("Enter the first number: "))
# val_2 = int(input("Enter the second number: "))
# for i in range((val_1-1), (val_2+1)):
#     if i % 7 == 0:
#         print(i)


# task_8
# val_1 = int(input("Enter the first number: "))
# val_2 = int(input("Enter the second number: "))
# count = 0
# for i in range((val_1-1), (val_2+1)):
#     print(f"The full range is: {i}")
#     if i%7 == 0:
#         print(f"Values which are divided by 7: {i}")
#     elif i%5 == 0:
#         count+=1
#         print(f"The quantity of values which are divided by 5: {count}")
#
# for i in reversed(range((val_1-1), (val_2+1))):
#     print(f"Reversed range is {i}")


#task9
val_1 = int(input("Enter the first number: "))
val_2 = int(input("Enter the second number: "))
while val_1 <= val_2:
    val_1 = val_1 + 1
    if val_1 % 3 == 0 and val_1 % 5 == 0:
        print(f"Fizz Buzz")
    elif val_1%3 == 0:
        print(f"Fizz")
    elif val_1%5 == 0:
        print(f"Buzz")
    else:
        print(f"{val_1}")



# a=1
# b=36
# while a <= b:
#     if a % 2 ==0:
#         print(a) #odd
#     a = a + 1