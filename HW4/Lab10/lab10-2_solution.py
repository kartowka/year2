### Our custom OOP
def make_class(attrs,class_name, base=None):
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
    #----------------
    cls['set']('class_name',class_name)
    cls['set']('class',cls)
    #----------------
    return cls

### class Point
# The Point class is created through a make_point_class function,
# which has structure similar to a class statement in Python,
# but concludes with a call to make_class.
def make_point_class():
    color = 'blue'

    def __init__(self, x=0, y=0):
        self['set']('x', x)
        self['set']('y', y)

    def str(self):
        return '(x=%d, y=%d)' % (self['get']('x'), self['get']('y'))

    def prt(self):
        print(self['get']('str')())

    def shift(self, number):
        self['set']('x', self['get']('x') + number)
        self['set']('y', self['get']('y') + number)

    def eq(self, other):
        return  self['get']('x') == other['get']('x')  and  self['get']('y') == other['get']('y')

    return make_class(locals(),'Point')

def make_color_point_class():
    color = 'red'

    def str(self):
        return Point['get']('str')(self) + " [color = %s]" % self['get']('color')

    return make_class(locals(),'Color Point',Point)


# ------------------------------------------------
def driver():    
    P=Point['new'](0,0)
    print(P)
    #{'set': <function make_class.<locals>.new.<locals>.set at 0x0000022A79F87620>,
    #'get': <function make_class.<locals>.new.<locals>.get at 0x0000022A79F87598>}
    P['get']('prt')() # => (x=0, y=0)  
    P1=P['get']('class')['new'](1,2) 
    print(P1)
    #{'set': <function make_class.<locals>.new.<locals>.set at 0x0000022A79F87730>,
    #'get': <function make_class.<locals>.new.<locals>.get at 0x0000022A79F876A8>}
    print(P['get']('class_name'))       # => Point
    print(Point['get']('class_name'))   # => Point
    print(P1['get']('class_name'))      # => Point
    P['get']('prt')()                   # => (x=0, y=0)
    P1['get']('prt')()                  # => (x=1, y=2)
    
# ------------------------------------------------        
Point =  make_point_class()
driver()
