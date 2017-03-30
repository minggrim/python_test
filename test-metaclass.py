from six import with_metaclass


class MetaClass(type):

    # __prepare__ only in python3
    @classmethod
    def __prepare__(metacls, name, parents, **kwargs):
        my_dict = {}
        print(
            'in __prepare__ return dict obj id {}'
            .format(id(my_dict))
        )
        print(
            'types : metacls {}, name {}, parents {}, kwargs {}'
            .format(
                type(metacls),
                type(name),
                type(parents),
                type(kwargs),
            )
        )
        print(
            'contents : metacls {}, name {}, parents {}, kwargs {}'
            .format(
                metacls,
                name,
                parents,
                kwargs,
            )
        )
        return my_dict

    def __new__(cls, name, parents, dct):
        print(
            'in __new__ dct id {}'
            .format(id(dct))
        )
        return super(MetaClass, cls).__new__(cls, name, parents, dct)

    def __init__(cls, name, parents, dct):
        print(
            'in __init__ dct id {}'
            .format(id(dct))
        )


# use MetaClass to build MyClass
class MyClass(with_metaclass(MetaClass)):
    pass
