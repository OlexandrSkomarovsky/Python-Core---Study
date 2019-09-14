"""
Задано чотирицифрове натуральне число. 
Знайти добуток цифр цього числа.
Записати число в реверсному порядку.
Посортувати цифри, що входять в дане число
"""
digit = input('please type four-digit natural number: ')
print("Добуток цифр цього числа: ", int(digit[0])*int(digit[1])*int(digit[2])*int(digit[3]))
list_of_digits = [int(digit[0]), int(digit[1]), int(digit[2]), int(digit[3])]
list_of_digits.reverse()
print("Число в реверсному порядку: ", str(list_of_digits[0])+str(list_of_digits[1])+str(list_of_digits[2])+str(list_of_digits[3]))
list_of_digits.sort()
print("Посортовані цифри, що входять в дане число: ", list_of_digits)
