def make_class(attrs,base=None):
    def get(name):
        if name in attrs: return attrs[name]
        elif base:        return base['get'](name)
    def set(name,value): attrs[name] = value

    def new(*args):
        attrs={}

        def get(name):
            if name in attrs:   return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj,*args)
                else:               return value

        def set(name,value):    attrs[name] = value

        obj = {'get': get, 'set':set }

        init = get('__init__')
        if init: init(*args)

        return obj

    cls = {'get': get, 'set': set, 'new': new }
    return cls

def make_point_class():
    color = 'blue'

    def __init__(self,x=0,y=0):
        self['set']('x',x)
        self['set']('y',y)
    
    def str(self):
        return '(x=%d,y=%d)' % (self['get']('x'),self['get']('y'))
    
    def prt(self):
        print(self['get']('str')())
    
    def shift(self,number):
        self['set']('x', self['get']('x')+number)
        self['set']('y', self['get']('y')+number)
    
    def eq(self,other):
        return self['get']('x') == other['get']('x') and self['get']('y') == other['get']('y')

    return make_class(locals())
def make_color_point_class():
    color='red'
    
    def str(self):
        return Point['get']('str')(self)+ ' [color = %s]' % self['get']('color')

    return make_class(locals(),Point)

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