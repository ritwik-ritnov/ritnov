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

def factorial(x):
    '''calculate factorial of an integer'''
    y=1
    print("factorial =",end=" ")
    while(x>0):
        y *= x
        x = x-1
    return y

#recursion
def fibonacci(x):
    '''f(n)=f(n-1)+f(n-2)'''
    if x==0:
        return 0
    if x==1:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)

#recursion
def factorialr(x):
    '''calculate factorial in recursive mode'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorialr(x-1)
