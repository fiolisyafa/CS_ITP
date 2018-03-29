import math
a = lambda a : a**2
b = lambda x, y: math.sqrt((x**2)+(y**2))
c = lambda *args: sum(args) / len(args)
d = lambda z: "".join(set(z))

aa = a(4)
bb = b(4, 5)
cc = c(4, 5, 6, 7)
dd = d("hello")
print(aa)
print(bb)
print(cc)
print(dd)

def aa(a):
    return a**2
def bb(x, y):
    return math.sqrt((x**2)+(y**2))
def cc(*args):
    return sum(args) / len(args)
def dd(z):
    return "".join(set(z))
