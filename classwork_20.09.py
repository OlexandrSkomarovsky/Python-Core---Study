'''
1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. 
'''
# def sered(*args):
#     print(sum(args)/len(args))
     
# sered(9, 4, 5, 1, 2, 3)
    
'''
2.  Написати функцію, яка повертає абсолютне значення числа.
'''
# def absolt(number):
#     print((number**2)**0.5)
# absolt(-5)
'''
3.  Написати функцію, яка знаходить максимальне число з двох чисел,
 а також в функції використати рядки документації DocStrings.
 '''
def maxim(arg1, arg2):
    ''' This function print the biggest number '''
    print(maxim.__doc__ , max(arg1, arg2))
     
maxim(99,9)

'''
4.  Написати програму, яка обчислює площу прямокутника, трикутника та кола (написати три функції 
для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)
'''
"""This program for counting area of rectangual, triangual and circul. For rect input 1, for triangual - 2, for circul - 3."""
shape = int(input())
# def s_rect(a,b):
#     return a*b
# def s_triangl(a,b,c):
#     p = (a+b+c)*0.5
#     return (p*(p-a)*(p-b)*(p-c)**0.5)
# def s_circule(r)
#     Pi = 3.14
#     return Pi*r**2