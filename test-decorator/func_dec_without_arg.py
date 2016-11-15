def my_dec(f):
    def d_f(*argv, **kwargv):
        print('before call')
        result = f(*argv, **kwargv)
        print('after call')
        return result

    return d_f

@my_dec
def print_dummy():
    print('dummy')

print_dummy()
#you can see print_dummy is not original print_dummy, it's my_dec_class object
print(print_dummy)
