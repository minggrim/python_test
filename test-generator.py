def my_generator(i):
    x = 0
    while x < i:
        print(x)
        yield
        x = x + 1

g = my_generator(10)
print(type(g))
for l in g:
    print(type(l))  # get None
    pass
