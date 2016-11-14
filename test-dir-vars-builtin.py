class A(object):
    a = 10


class B(object):
    b = 20

class C(A, B):
    c = 30

ccc = C()
ccc.d = 40

#vars print key/value pairs

#see current namespace
print(vars())
print('---')
#you can see the equivalence
print(vars(ccc))
print(ccc.__dict__)
print('---')
print(vars(A))
print(A.__dict__)
print('---')
print(vars(B))
print(B.__dict__)
print('---')
print(vars(C))
print(C.__dict__)
print('---')
print(vars(object))
print(object.__dict__)
print('---')
#print all attributes(key) recursively
#ccc -> C -> A -> B ( not include object)
print(dir(ccc))

