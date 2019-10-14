'''
1.  Спробуйте переписати наступний код через map. Він приймає список реальних імен і замінює їх хеш-прізвищами, використовуючи  більш надійний метод-хешування.

names = ['Sam', 'Don', 'Daniel'] 
for i in range(len(names)): 
    names[i] = hash(names[i]) 
print(names) 

# => [6306819796133686941, 8135353348168144921, -1228887169324443034]
'''
# names = ['Sam', 'Don', 'Daniel'] 
# hash_names = map(lambda x: hash(hash_names), names)
# print(list(hash_names))

'''
2.  Вивести список кольору “red”, який найчастіше зустрічається в даному списку 
 [“red”, “green”, “black”, “red”, “brown”, “red”, “blue”, “red”, “red”, “yellow” ] 
 використовуючи функцію filter.
 '''
# lst = ['red', 'green', 'black', 'red', 'brown', 'red', 'blue', 'red', 'red', 'yellow'] 
# def red_(i):
#     return i == 'red'
# # lst_red = filter(red_, lst)
# lst_red = filter(lambda x: red_(x), lst)
# print(list(lst_red))

'''
3. Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’],
 перетворити цей список  в список, всі числа якого мають тип даних integer:
1)  використовуючи метод  append
2)  використовуючи метод  map
'''
# lst = ['1','2','3','4','5','7']
# 1)
# int_lst = [] 
# for i in lst:
#     int_lst.append(int(i))
# print(int_lst)
# 2)
# int_lst = map(int, lst)
# print(list(int_lst))

'''4. Перетворити список, який містить милі ,  в список, який містить кілометри (1 миля=1.6 кілометра)
   a) використовуючи функцію map
  b) використовуючи функцію map та lambda
'''
# def ml_km(ml):
#     return round(float(ml)*1.6, 2)
# myli = [2, 3, 5, 3]
# # km = map(ml_km, myli)
# # print(list(km))
# km = map(lambda x: round(float(x)*1.6, 2), myli)
# print(list(km))
'''5.  Знайти найбільший елемент в списку  використовуючи функцію reduce'''
# lst = [1, 2, 6, 4, 7, 5, 2]
# max_ = reduce(lambda x: expression)
'''6. Перепишіть наступний код, використовуючи map, reduce і filter. Filter приймає функцію і колекцію. Повертає колекцію тих елементів, для яких функція повертає True.
people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}] 
height_total = 0 
height_count = 0 
for person in people: 
    if 'height' in person: 
        height_total += person['height'] 
        height_count += 1 
print(height_total)'''