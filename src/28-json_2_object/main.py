class obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, obj(b) if isinstance(b, dict) else b)

if __name__ == '__main__':
    d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
    x = obj(d)
    print(d, type(d), x, type(x))
    print(x.b.c)