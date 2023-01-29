def is_leap(year):
    '''check leap year'''
    if year%100==0:
        if year%400==0:
            leap = True
        else:
            leap = False
    elif year%4==0:
        leap = True
    else:
        leap = False
    return leap


def tex(x):
    '''if n=5, it will print 12345.....n'''
        a = 1
        while a<x:
            print(a,end="")
            a = a+1
    return a

def starx(x):
    '''print pattern: for x=5, star= *****'''
    star = x*"*"
    return star
