'''
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
double_char("String") ==> "SSttrriinngg"
double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
double_char("1234!_ ") ==> "11223344!!__  "
'''
def double_char(s):
    l = [i*2 for i in s]
    l = ''.join(l)
    return l