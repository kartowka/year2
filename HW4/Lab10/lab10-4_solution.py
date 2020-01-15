### Ex4: define a top-level "object" class with an __init__ method,
###      simplify make_class, since now __init__ always exists.
###      (this is also more correct, since we shouldn't accept 'new'
###      with arbitrary args if __init__ is not explicitly defined.)
# top_object is defined via make_class, so can't have default
# inheritance from top_object -- use an "else "in "get" instead.

def make_class(attrs, base):
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
        #--------
        init(*args)
        #--------

        return obj

    # class dictionary
    cls = { 'get': get, 'set': set, 'new': new }
    return cls

def make_top_class():
    def __init__(self): pass
    return make_class(locals(),None)

def make_point_class():
    color = 'blue'
    def __init__(self, x=0, y=0):
        self['set']('x', x)
        self['set']('y', y)
    def str(self):
        return '(x=%d, y=%d)' % (self['get']('x'),self['get']('y'))
    def prt(self):
        print(self['get']('str')())
    def shift(self,number):
        self['set']('x',self['get']('x')+number)
        self['set']('y',self['get']('y')+number)
    def eq(self,other):
        return self['get']('x') == other['get']('x') and self['get']('y') == other['get']('y')

    # locals() returns a dictionary of local variables
    return make_class(locals(),make_top_class())


# ------------------------------------------------
# Color Point Class
# ------------------------------------------------
def make_color_point_class():
    color = 'red'
    def str(self):
        return Point['get']('str')(self)+' [color=%s]' % self['get']('color')

    return make_class(locals(),Point)

# ------------------------------------------------
def driver():    
    p = Point['new'](1, 2)
    q = ColorPoint['new'](3, 4)
    q2 = ColorPoint['new'](5, 6)
    p['get']('prt')()
    q['get']('prt')()
    p['get']('shift')(3)
    p['get']('prt')()
    print(q['get']('eq')(q))
    q['set']('color', 'green')
    q['get']('prt')()
    q2['get']('prt')()


Point      = make_point_class()
ColorPoint = make_color_point_class()
driver()
