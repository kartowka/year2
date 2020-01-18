from math import gcd

class Rlist(object):
    """A recursive list consisting of a first element and the rest."""
    class EmptyList(object):
        def __len__(self):
            return 0
    empty = EmptyList()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
    def __repr__(self):
        args = repr(self.first)
        if self.rest is not Rlist.empty:
            args += ", {0}".format(repr(self.rest))
        return 'Rlist({0})'.format(args)
    def __len__(self):
        return 1 + len(self.rest)
    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i-1]
    def __add__(self, other):
        return coerce_apply('add', self, other)
    def __mul__(self, other):
        return coerce_apply('mul', self, other)
def extend_rlist(s1, s2):
    if s1 is Rlist.empty:
        return s2
    return Rlist(s1.first, extend_rlist(s1.rest, s2))
def map_rlist(s, fn):
    if s is Rlist.empty:
        return s
    return Rlist(fn(s.first), map_rlist(s.rest, fn))
def filter_rlist(s, fn):
    if s is Rlist.empty:
        return s
    rest = filter_rlist(s.rest, fn)
    if fn(s.first):
        return Rlist(s.first, rest)
    return rest

class Rational(object):
    """A rational number represented as a numerator and denominator."""

    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)
    def __add__(self, other):
        return coerce_apply('add', self, other)
    def __mul__(self, other):
        return coerce_apply('mul', self, other)



# ---------------------------------------------------------
def add_rational(x, y):
    """Add rational numbers x and y."""
    nx, dx = x.numer, x.denom
    ny, dy = y.numer, y.denom
    return Rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    """Multiply rational numbers x and y."""
    return Rational(x.numer * y.numer, x.denom * y.denom)

# ---------------------------------------------------------

# -----------------------------------------------------------
def add_rlist(x,y):
    """add rlist numbers x and y."""
    return extend_rlist(x,y)

# -------------------------------------------------------------

# ------------------------------------------------------------------

def add_int(x,y):
    """add int numbers x and y."""
    return x+y
def mul_int(x,y):
    """Multiply int numbers x and y."""
    return x*y


# ------------------------------------------------------------------

def add(z1, z2):
    """Add z1 and z2, which may be complex or rational."""
    types = (type_tag(z1), type_tag(z2))
    return add.implementations[types](z1, z2)

def type_tag(x):
    """Return the tag associated with the type of x."""
    return type_tag.tags[type(x)]


type_tag.tags = {int: 'int', Rlist: 'rlist', Rational:  'rat'}

def add_int_rational(i,r):
    """add int and rational numbers int and rational"""
    return Rational(i*r.denom+r.numer,r.denom)

def add_rational_rlist(r,rl):
    """add rational and rlist numbers rl and r"""
    args = repr(rl.first)
    if rl.rest is not Rlist.empty:
        args += ", {0}".format(add_rational_rlist(r,rl.rest))
    if rl.rest is Rlist.empty:
        """if the point was sending the repr of Rational(val1,val2) just need to send instead of r -> repr(r)"""
        args+=', Rlist({})'.format(r)
    return 'Rlist({0})'.format(args)

add_rlist_rational = lambda rl,r: add_rational_rlist(r,rl)

add_rational_and_int = lambda r,i: add_int_rational(i,r)

add.implementations = {}
add.implementations[('rat', 'rlist')] = add_rational_rlist 
add.implementations[('rlist', 'rlist')] = add_rlist 
add.implementations[('rat', 'rat')] = add_rational 
add.implementations[('int', 'int')] = add_int 
add.implementations[('int', 'rat')] = add_int_rational 

def apply(operator_name, x, y):
    """Apply an operation ('add' or 'mul') to x and y."""
    tags = (type_tag(x), type_tag(y))
    key = (operator_name, tags)
    return apply.implementations[key](x, y)

def mul_int_rlist(i,rl):
    """multiply int rlist on i,rl"""
    print(type(i))
    if type(i)!=int:
        i=i[0]
    print(type(i))
    args=rl
    for _ in range(0,i):
        args=extend_rlist(args,rl)       
    return args
     
def mul_int_rational(i,r):
    """multiply int rational on i,r """
    return Rational(i*r.numer,r.denom)

mul_rlist_int = lambda rl,i: mul_int_rlist(i,rl)
mul_rational_int = lambda r,i: mul_int_rational(i,r)


apply.implementations = {('mul', ('int', 'rlist')): mul_int_rlist,
                         ('mul', ('rat', 'rat')): mul_rational,
                         ('mul', ('int', 'int')): mul_int,
                         ('mul', ('int', 'rat')): mul_int_rational}

### add 'add' implementations from add.implementations to apply.implementations
adders = add.implementations.items()
apply.implementations.update({('add', tags):fn for (tags, fn) in adders})

def rational_to_rlist(r):
    return Rlist(r.numer/r.denom)
def int_to_rational(i):
    return Rational(i,1)
def int_to_rlist(i):
    return Rlist(i)

coercions = {('rat', 'rlist'): rational_to_rlist,
            ('int','rat'): int_to_rational,
            ('int','rlist'):int_to_rlist}

def coerce_apply(operator_name, x, y):
    """Apply an operation ('add' or 'mul') to x and y."""
    tx, ty = type_tag(x), type_tag(y)
    if tx != ty:
        if (tx, ty) in coercions:
            tx, x = ty, coercions[(tx, ty)](x)
        elif (ty, tx) in coercions:
            ty, y = tx, coercions[(ty, tx)](y)
        else:
            return 'No coercion possible.'
    assert tx == ty
    key = (operator_name, tx)
    return coerce_apply.implementations[key](x, y)

coerce_apply.implementations = {('add', 'rlist'): add_rlist,
                                ('add', 'rat'): add_rational,
                                ('mul', 'rat'): mul_rational,
                                ('mul', 'rlist'): mul_rlist_int}

s = Rlist(3, Rlist(4, Rlist(5)))
x=int_to_rlist(4)

print(s*2)