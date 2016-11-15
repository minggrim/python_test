def my_dec(arg1, arg2):
    def outer_d_f(f):
        def d_f(*argv, **kwargv):
            print('before call {} {}'.format(arg1, arg2))
            result = f(*argv, **kwargv)
            print('after call')
            return result
        return d_f
    return outer_d_f

@my_dec('test1', 'test2')
def print_dummy():
    print('dummy')

print_dummy()
#you can see print_dummy is not original print_dummy, it's d_f
print(print_dummy)
