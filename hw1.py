# Anthony Eitan Fleysher
# ID: 203192331

#EX1 - done

def parseStr(str):
    """this function accept numeric string and convert(return) it to decimal number,function didn`t accept alphbet"""
    newNum=0
    dig=0
    flag=False
    for _ in str:
        if(_=='-'):
            flag=True
        elif(_<'0' or _>'9'):
            return -1
        else:
            dig=ord(_)-ord('0')
            newNum=newNum*10+dig
    if(flag==True):
        newNum*=-1
    return newNum

print("EX1 - Enter number as String.")
num=input("enter number: ")
print(parseStr(num))

#EX7 - done

def evenFactorial(n):
    """recursivly return sum of even factorials"""
    if(n<=0):
        return 1
    if(n%2==0):
        return n*evenFactorial(n-1)
    return evenFactorial(n-1)

print("EX7 - Enter number > 0.")
n=int(input("enter number between 1-9: "))
print(evenFactorial(n))


#EX6 - done

def printBin(number):
    """recursivly convert number from dec to bin """
    if(number==0):
        return 0
    return number%2+10*(printBin(int(number/2)))

print("EX6 - Enter number to convert to binary.")
number=int(input("enter number to convert: "))
print(printBin(number))



#EX3 - done

def interceptPoint(m1,n1,m2,n2):
    """finds the interept point between 2 lines"""
    mx=m2-m1
    my=n2-n1
    if(mx==0):
        return None
    m=my/mx
    if(m<0):
        m*=-1
    y=m*m1+n1
    point=(m,y)
    return point

print("EX3 - enter 4 points as follow n1 n2 n3 n4.")
m1,n1,m2,n2=[int(x) for x in input("enter numbers for m1,n1,m2,n2: ").split()]
print(interceptPoint(m1,n1,m2,n2))


#EX4 - done

def factorSum(n):
    """check for prime Numbers in number"""
    sum=0
    for i in range(2,n+1):
        if(n % i == 0):
            isPrime=1
            for j in range(2, (i//2+1)):
                if(i % j == 0):
                    isPrime = 0
                    break

            if(isPrime==1):
                sum+=i
    return sum

print("EX4 - enter number checks for primes.")
number=int(input("enter number: "))
print(factorSum(number))

#EX2 - done

def smallHash(s):
    an=s[0]
    aPrev=s[0]
    if(len(s)==1):
        return an
    for i in range(1,len(s)):
        an=((31*aPrev)^s[i])&0xFF
        aPrev=an
    return an

print("EX2 - enter numbers [0,255] calc Hash.")
a=[(int(x)%255) for x in input("enter elements of list: ").split()]
print(smallHash(a))


#EX5 - done

def checkBrackets(s,sum=0):
    """return True if the parentheses is string s match, otherwise False"""
    if s=="":
        return sum==0
    if sum<0:
        return False
    if s[0]=='(':
        return checkBrackets(s[1:],sum+1)
    if s[0]==')':
        return checkBrackets(s[1:],sum-1)
    return checkBrackets(s[1:],sum)

print("EX5 - check for parentheses match.")
brackets=input("enter string: ")
print(checkBrackets(brackets))
