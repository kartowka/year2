import copy
# ------------------------------------------------
# Copy and Deepcopy
# ------------------------------------------------
#
# ----------------- Copy -------------------------
#test1=[1,2,3,[1,2,3]]
#test1 # => [1, 2, 3, [1, 2, 3]]
#test_copy=copy.copy(test1)
#test1, test_copy # => ([1, 2, 3, [1, 2, 3]], [1, 2, 3, [1, 2, 3]])
#test_copy[3].append(4)
#test1, test_copy # => ([1, 2, 3, [1, 2, 3, 4]], [1, 2, 3, [1, 2, 3, 4]])
#test_copy.append(5)
#test1, test_copy # =>([1, 2, 3, [1, 2, 3, 4]], [1, 2, 3, [1, 2, 3, 4], 5])

# ----------------- DeepCopy ---------------------
#test1=[1,2,3,[1,2,3]]
#test_deepcopy = copy.deepcopy(test1)
#test_deepcopy[3].append(4)
#test1, test_deepcopy # => ([1, 2, 3, [1, 2, 3]], [1, 2, 3, [1, 2, 3, 4]])

# ----------------- Class ------------------------
class Class1(object):
    def __init__(self, n1=0, n2=0, str1='None'):
        self.num1 = n1
        self.num2 = n2
        self.str = str1
    def printC(self):
        print(self.num1, self.num2, self.str)
# ------------------------------------------------
#t1 = Class1(2,3)
#t1.printC()    # => 2 3 None
#t2=t1
#t2.printC()    # => 2 3 None
#t1.str = 'Test'
#t1.printC()    # => 2 3 Test
#t2.printC()    # => 2 3 Test
# ------------------------------------------------
#t1 = Class1(2,3)
#t3 = copy.copy(t1)
#t3.printC()    # => 2 3 None
#t1.str = 'Test'
#t1.printC()    # => 2 3 Test
#t3.printC()    # => 2 3 None


# ------------ Class Attributes ------------------
#hasattr(t1,'num2') # => True
#hasattr(t1,'num3') # => False
#t1.__dict__        # => {'num1': 2, 'str': 'Test', 'num2': 3}

#for attr in t1.__dict__:
#	print( attr,getattr(t1,attr))	
#num1 2
#str Test
#num2 3


