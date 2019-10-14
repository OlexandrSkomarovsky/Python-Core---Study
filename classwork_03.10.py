'''
1.  Напишіть програму, яка пропонує користувачу ввести ціле число
#  і визначає чи це число парне чи непарне, чи введені дані коректні.
# '''
# class Chysla:
#     def __init__(self, number):
#         self.number = number
#         self.number = input("Pleas input number: ")
#     def perev(self):
#         try:   
#            self.number is int 
#         except ValueError:
#             print("ValueError!")
#         else:
#             if self.number % 2 == 0:
#                 print("This number is even number")
#             else:
#                 print("This number is not even number")
#         finally:
#             print("executing finally clause")
# a = Chysla()
try: 
    number = int(input("enter your number:"))
    if number % 2 ==0:
        print("This number is even number")
    else:
        print("This number is not even number")
except ValueError:
    print("ValueError!")
finally:
    print("executing finally clause")
"""2.  Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить 
повідомлення про те чи вік є парним чи непарним числом. Необхідно передбачити можливість введення
 від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію. Головний код має викликати
  функцію, яка обробляє введену інформацію."""
age = int(input("Pleas enter your age:"))
while type(age) != int:
    try:   
       age = int(age)
    except ValueError:
        print("ValueError!")
    finally:
        print("executing finally clause")
if age < 0:
    try:   
        raise ValueError("That is not a positive number!") 
    except ValueError as neg: 
        print(neg) 
    finally: 
        print("executing finally clause")
            
if number % 2 ==0:
    print("This number is even number")
else:
    print("This number is not even number")



