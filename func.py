#check leap year
def is_leap(year):
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

#if n=5, it will print 12345.....n
def tex(x):
        a = 1
        while a<x:
            print(a,end="")
            a = a+1
    return a
