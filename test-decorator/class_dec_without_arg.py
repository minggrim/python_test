class my_dec_class(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *argv, **kwargv):
        print('before call')
        result = self.f(*argv, **kwargv)
        print('after call')
        return result

@my_dec_class
def print_dummy():
    print('dummy')

print_dummy()
#you can see print_dummy is not original print_dummy, it's my_dec_class object
print(print_dummy)
