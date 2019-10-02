'''
Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished For Loop!
'''
def create_array(n):
    res=[]
    i=1
    for i in range(1, n+1): res+=[i]
    return res