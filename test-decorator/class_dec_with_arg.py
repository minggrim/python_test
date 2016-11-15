class my_dec_class(object):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, f):
        def d_f(*argv, **kwargv):
            print('before call {} {}'.format(self.arg1, self.arg2))
            result = f(*argv, **kwargv)
            print('after call')
            return result
        return d_f

@my_dec_class('test1', 'test2')
def print_dummy():
    print('dummy')

print_dummy()
#you can see print_dummy is not original print_dummy, it's d_f
print(print_dummy)

