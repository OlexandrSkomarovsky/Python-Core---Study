'''
1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.
'''
# spysok_tc = [input('Vvedit chyslo: ') for v in range(int(input('skilky chysel: ')))]
# print('мінімальне число:', min(spysok_tc), 'максимальне число: ', max(spysok_tc))
'''
2.  В інтервалі від 1 до 10 визначити числа 
•  парні, які діляться на 2,
•  непарні, які діляться на 3, 
•  числа, які не діляться на 2 та 3.
'''
# spysok = [ i for i in range(1,11) if i % 2 == 0 ]
# print(spysok)
# spysok = [ i for i in range(1,11) if i % 2 == 1 and i % 3 == 0 ]
# print(spysok)
# spysok = [ i for i in range(1,11) if i != 5 and i % 2 == 1 and i % 3 == 1,  i % 2 == 1 or i % 3 == 1 ]
# print(spysok)
# for x in range(1,11):
#     if x % 2 == 0:
#         print(x, 'is even multiply of 2')
#     elif x % 3 == 0:
#         print(x, 'is even multiply of 3')
#     else:
#         print(x, 'not didvisible by 3 and 2')
'''
3.  Написати програму, яка обчислює факторіал числа, яке 
користувач вводить.(не використовувати рекурсивного виклику функції)
'''
# faktorial = range(1, int(input("Pleas enter number faktorial:")) + 1 )
# result = 1
# for x in faktorial:
#     result *= x
# print("Faktorial number:", result )
'''
4.  Напишіть скрипт, який перевіряє логін, який вводить користувач. 
Якщо логін вірний (First), то привітайте користувача. 
Якщо ні, то виведіть повідомлення про помилку. 
(використайте цикл while)
'''
# while True:
#     login = input('Pleas enter login: ')
#     if not login == 'First':
#         print('Mistake')
#     else:
#         print('Welcome')
#         break
        

