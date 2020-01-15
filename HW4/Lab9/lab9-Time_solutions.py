import copy
'''
Assignment statements in Python do not copy objects, they create bindings between a target and an object. 
For collections that are mutable or contain mutable items, a copy is sometimes needed so one can change one copy without changing the other. 
copy.copy(x)
    Return a shallow copy of x.
copy.deepcopy(x)
    Return a deep copy of x.
'''


class Time():
    """represents the time of day attributes: hour, minute, second"""

    # constructor
    def __init__(self, h=0, m=0, s=0):
        self.hour   = h  if h>=0 and h<=23  else 0
        self.minute = m  if m>=0 and m<=59  else 0
        self.second = s  if s>=0 and s<=59  else 0

    # utilities
    def printTime(self):
        print('%02d:%02d:%02d' % (self.hour,self.minute,self.second))
   
    def TimeToInt(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes   * 60 + self.second
        return seconds
    
    def IntToTime(self, s):
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        h    = h % 24
        return Time(h, m, s)

    # operators
    def Later(self, other):
            return self.TimeToInt() > other.TimeToInt()

    def addSecond(self):
        return self.IntToTime(self.TimeToInt() + 1)

    def __add__(self, other):
        return self.IntToTime(self.TimeToInt() + other.TimeToInt())

    def __sub__(self, sec=1):
        return self.IntToTime(self.TimeToInt() - sec)

    def __str__(self):
        return '%02d:%02d:%02d' % (self.hour, self.minute, self.second)


class ZoneTime(Time):
    def __init__(self, h=0, m=0, s=0, ZoneName='Jerusalem'):
        Time.__init__(self, h, m, s)
        self.name=ZoneName

    def printTime(self):
        Time.printTime(self)
        print('%s  ' % (self.name))


def main():
    start = Time(9,45, 0)
    end   = Time(1,35, 0)
    test  = Time(1,10,15)
    start.printTime()#09:45:00
    print(start)#09:45:00
    print("-----")
    Time.printTime(start)#09:45:00
    print("-----")

    print(start.Later(end))#True
    print(test.TimeToInt())#4215
    print("-----")
    
    help = test.IntToTime(4215)
    help.printTime()#01:10:15
    help = help.addSecond()
    help.printTime()#01:10:16
    print("-----")
    
    (start+end).printTime()# 09:45:00  +  01:35:00 = 11:20:00
    (help - 5).printTime()#01:10:11

    print(help.__str__())#01:10:16

    print("inheritance")
    child = ZoneTime(10,5,34,'Montreal')
    zt=ZoneTime(10,55,34)#10:55:34 \n Jerusalem
    print("-----")

    zt.printTime()
    print("-----")

    child.printTime()#10:05:34 \n  Montreal  

    print("---------- debugging -------------")
    print(type(start))#<class '__main__.Time'>

    cop=copy.copy(start)
    print(cop)#09:45:00
    print(type(cop))#<class '__main__.Time'>
    print(start.__class__)#<class '__main__.Time'>
    print(hasattr(start,'second'))#True
    print(hasattr(start,'sec'))#False

    # access the attributes of an object
    print(start.__dict__)#{'hour': 9, 'second': 0, 'minute': 45}
    #A special attribute of every module is __dict__. This is the dictionary containing the modules symbol table.
    def print_all_attributes(obj):
        for attr in obj.__dict__:
            print(attr,getattr(obj,attr))

    print_all_attributes(start)
    #hour 9
    #second 0
    #minute 45


main()    
