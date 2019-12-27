# ID : 203192331
# Name : Anthony Eitan Fleysher

#Exercise 3
def newtow(f,Df,x0,epsilon,max_iter):
    min_iter=0
    if Df(x0)==0:
        return 'No Answer'
    x=f(x0)/Df(x0)
    while abs(x)>epsilon and min_iter<max_iter:
        x=f(x0)/Df(x0)
        x0=x0-x
        min_iter=min_iter+1
    if(min_iter==max_iter):
        return "Exceeded maximum iteration.No solution found"
    return ("the solution was found after {} iteration: {}".format(min_iter,x0))

f=lambda x:x**(1/3)
Df=lambda x:(1/3)*x**(-2/3)
answer=newtow(f,Df,0.1,1e-2,100)
print(answer)

# Exercise 4
first=lambda x:x**3
second=lambda x:x+1
def composition(f,g):
    return lambda h:f(g(h))

add_one_and_power=composition(first,second)
result=add_one_and_power(12)
print(result)

add_one_and_power=composition(second,first)
result=add_one_and_power(12)
print(result)
