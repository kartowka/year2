#exercise 1
x=10

def sum(x):
    if x<=1:
        return 1
    return x+sum(x-1)

print(sum(10))


#exercise 2
import time
x=int(input("enter which fibo you want? "))
def fibo(x):
    if(x<=1):
        return x
    return fibo(x-1)+fibo(x-2)

def fibtime(x):
    start = time.time()
    fibo(x)
    end = time.time()
    return(end - start)

print(fibtime(x))

#exercise 3

def digCount(x):
    if(abs(x)<10):
        return 1
    return 1+digCount(x/10)

print(digCount(-123.12))
