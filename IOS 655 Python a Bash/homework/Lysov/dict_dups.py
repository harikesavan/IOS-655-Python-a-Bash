L = [
    {'x':3, 'y':3},{'x':2, 'y':-1},{'x':2, 'y':3},{'x':-1, 'y':0},{'x':2, 'y':2},
    {'x':3, 'y':-1},{'x':1, 'y':2},{'x':0, 'y':2},{'x':1, 'y':0},{'x':0, 'y':-1},
    {'x':0, 'y':1},{'x':-1, 'y':0},{'x':1, 'y':-1},{'x':-1, 'y':1},{'x':2, 'y':0},
    {'x':1, 'y':2},{'x':-1, 'y':0},{'x':1, 'y':2},{'x':-1, 'y':3},{'x':-1, 'y':2},
    {'x':0, 'y':0},{'x':1, 'y':3},{'x':2, 'y':0},{'x':0, 'y':2},{'x':-1, 'y':-1},
    {'x':0, 'y':2},{'x':2, 'y':3},{'x':2, 'y':-1},{'x':2, 'y':0},{'x':3, 'y':3},
    {'x':-1, 'y':0},{'x':2, 'y':-1},{'x':0, 'y':-1},{'x':2, 'y':2},{'x':-1, 'y':0},
    {'x':2, 'y':-1},{'x':0, 'y':1},{'x':0, 'y':3},{'x':3, 'y':1},{'x':0, 'y':2},
    {'x':2, 'y':0},{'x':0, 'y':2},{'x':1, 'y':2},{'x':0, 'y':3},{'x':1, 'y':0},
    {'x':-1, 'y':0},{'x':-1, 'y':3},{'x':1, 'y':-1},{'x':0, 'y':2},{'x':2, 'y':3},
    {'x':-1, 'y':1},{'x':1, 'y':0},{'x':2, 'y':3},{'x':2, 'y':2},{'x':1, 'y':2},
    {'x':0, 'y':-1},{'x':-1, 'y':1},{'x':1, 'y':0},{'x':0, 'y':2},{'x':3, 'y':3},
    {'x':2, 'y':-1},{'x':1, 'y':3},{'x':2, 'y':3},{'x':1, 'y':2},{'x':3, 'y':0},
    {'x':0, 'y':2},{'x':3, 'y':0},{'x':0, 'y':-1},{'x':3, 'y':3},{'x':1, 'y':3},
    {'x':-1, 'y':-1},{'x':1, 'y':1},{'x':0, 'y':3},{'x':3, 'y':-1},{'x':1, 'y':2},
    {'x':1, 'y':0},{'x':-1, 'y':0},{'x':2, 'y':3},{'x':1, 'y':-1},{'x':0, 'y':0},
    {'x':0, 'y':1},{'x':1, 'y':1},{'x':-1, 'y':1},{'x':-1, 'y':0},{'x':2, 'y':-1},
    {'x':1, 'y':-1},{'x':3, 'y':-1},{'x':2, 'y':1},{'x':0, 'y':1},{'x':1, 'y':1},
    {'x':3, 'y':1},{'x':2, 'y':3},{'x':1, 'y':3},{'x':1, 'y':3},{'x':1, 'y':-1},
    {'x':2, 'y':1},{'x':0, 'y':1},{'x':3, 'y':0},{'x':1, 'y':-1},{'x':3, 'y':-1}
    ]

# we make unique list of dictionary items within a list
# by converting them first to tuples and adding them to a set, which is always unique
# and then converting them back to dictionaries from tuples and adding them to a list
L = list( dict(t) for t in (set( tuple(d.items()) for d in L)) )

print(L)
    