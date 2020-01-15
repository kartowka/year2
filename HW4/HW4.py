### Our custom OOP
def make_class(attrs, base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""
    #print(attrs)
    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs: return attrs[name]
        elif base:        return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value): attrs[name] = value

    # Return a new initialized objec'aaa': 5.5t instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:       return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else:               return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):       attrs[name] = value

        # instance dictionary
        obj = { 'get': get, 'set': set }

        # calls constructor if present
        init = get('__init__')
        if init: init(*args)

        return obj

    # class dictionary
    cls = { 'get': get, 'set': set, 'new': new }
    return cls


def make_data_class():
    def __init__(self,day=1,month=1,year=2020):
        self['set']('year',self['get']('setYear')(year))
        self['set']('month',self['get']('setMonth')(month))
        self['set']('day',self['get']('setDay')(day))
    def str(self):
        print('%02d.%02d.%d' % (self['get']('day'),self['get']('month'),self['get']('year')))
    def repr(self):
        return #TODO->repr(self['get']('str')())
    def getDay(self):
        return self['get']('day')
    def getMonth(self):
        return self['get']('month')
    def getYear(self):
        return self['get']('year')
    def setDay(self,day):
        if day>=1 and day<=30: self['set']('day',day)
        else: self['set']('day',1)
        return self['get']('day')
    def setMonth(self,month):
        if month>=1 and month<=12: self['set']('month',month)
        else: self['set']('month',1)
        return self['get']('month')
    def setYear(self,year):
        if year>=1900 and year<=2100: self['set']('year',year)
        else: self['set']('year',2020)
        return self['get']('year')
    return make_class(locals())

def make_person_class():
    def __init__(self,first,last,date,id):
        self['set']('first',self['get']('setFirst')(first))
        self['set']('last',self['get']('setLast')(last))
        self['set']('id',self['get']('setID')(id))
        self['set']('date',date)
    def str(self):
        print("Name: %s %s" % (self['get']('first'),self['get']('last')))
        print("DoB:")
        #TODO-> self['get']('date')['get']('str')()
        print("ID: %d" % (self['get']('id')))
    def getFirst(self):
        return self['get']('first')
    def getLast(self):
        return self['get']('last')
    def getID(self):
        return self['get']('id')
    def setFirst(self,first):
        if first: self['set']('first',first)
        else:   self['set']('first','John')
        return self['get']('first')
    def setLast(self,last):
        if last: self['set']('last',last)
        else:              self['set']('last','Doe')
        return self['get']('last')
    def setID(self,id):
        if id>0: self['set']('id',id)
        else: self['set']('id',0)
        return self['get']('id')
    return make_class(locals())
def make_student_class():
    def __init__(self,learning,avg,seniority):
        self['set']('learning',learning)
        self['set']('avg',avg)
        self['set']('seniority',seniority)
    def getLearning(self):
        return self['get']('learning')
    def getAvg(self):
        return self['get']('avg')
    def getSeniority(self):
        return self['get']('seniority')
    def setLearning(self,learning):
        if learning: self['set']('learning',learning)
        else: self['set']('learning','undefined')
        return self['get']('learning')
    def setAvg(self,avg):
        if avg>0: self['set']('avg',avg)
        else: self['set']('avg',0)
        return self['get']('avg')
    def setSeniority(self,seniority):
        if seniority>0:self['set']('seniority',seniority)
        else: self['set']('seniority',0)
        return self['get']('seniority')
    def str(self):
        print(Person['get']('str')(self))
        print("Learning: %s" % self['get']('learning'))
        print("Avg: %d" % self['get']('avg'))
        print("Seniority: %s" % self['get']('seniority'))
    return make_class(locals(),Person)
 
 
def driver():
    d1 = MyDate['new'](5,10,1991)
    d1['get']('str')()
    p1= Person['new']('Anthony','Fleysher',d1,203192331)
    p1['get']('str')()
    s1= Student['new']('Soft',98,3)
    s1['get']('str')()

    
MyDate     = make_data_class()
Person     = make_person_class()
Student    = make_student_class()
driver()