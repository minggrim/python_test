class my_iterator(object):

    def __init__(self, i):
        self.i = i
        self.x = 0

    def __iter__(self):
        return self

    def next(self):
        if self.x < self.i:
            print(self.x)
            self.x = self.x + 1
        else:
            raise StopIteration()


g = my_iterator(10)
print(type(g))
for i in g:
    print(type(i))  # get None
    pass
