class aaa(object):
    def abc(a, b, c, d):
        print(a)
        print(b)
        print(c)
        print(d)

    @classmethod
    def abc2(a, b, c, d):
        print(a)
        print(b)
        print(c)
        print(d)

    @staticmethod    
    def abc3(a, b, c, d):
        print(a)
        print(b)
        print(c)
        print(d)

a = aaa()
a.abc(1, 2, 3) #implicitly pass object reference
a.abc2(1, 2, 3)#implicitly pass class reference
a.abc3(1, 2, 3, 4)
