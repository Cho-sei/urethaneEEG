def namedlist(list_name, member_list)#, *, default=None):
#    if default is not None and len(member_list) == len(default):
#        member_dict = {member:value for member, value in zip(member_list, default)}
#    elif default is None:
#        member_dict = {member:None for member in member_list}
#    else:
#        raise RuntimeError("failed to create namedlist "+list_name+".")

    index_dict = dict(zip(member_list, range(len(member_list))))

    def set_classname(name ,bases, dict):
        return type(list_name, bases, dict)

    class NamedList(list, metaclass=set_classname):
        __index_dict = index_dict
#        exec(
#            "def __new__(cls, {}):return list.__new__(cls, [{}])".format(
#            ''.join(["{}={},".format(member, value) for member, value in member_dict.items()]),
#            ','.join(member_list)
#            )
#        )
#        exec(
#            "def __init__(self, {}):list.__init__(self, [{}])".format(
#            ''.join(["{}={},".format(member, value) for member, value in member_dict.items()]),
#            ','.join(member_list)
#            )
#        )
        def __init__(self, default=None):
            if default is None or len(default) != len(member_list):
                super().__init__([None]*len(member_list))
            elif len(default) == len(member_list):
                super().__init__(default)
            else:
                raise RuntimeError("The number of initial elements should be equal to the number of members.")

        def __get__(self, key):
            return self[index_dict[key]]

#        @classmethod
#        def getp(cls, x, p):
#            return x[cls.__index_dict[p]]
#
#        @classmethod
#        def indexp(cls, p):
#            return cls.__index_dict[p]

        def __set__(self, key, value):
            self[index_dict[key]] = value

    for member in member_list:
        setattr(NamedList, member, property(
            lambda self, p=member:self.__get__(p), lambda self, value, p=member:self.__set__(p, value)
        ))

#    NamedList.__name__ == list_name
    NamedList._fields = [member_list]

    return NamedList

if __name__ == "__main__":
    TestList = namedlist("TestList", ['a', 'b', 'c'])
    print(TestList)
    print(TestList.__name__)
    tl = TestList([1, 2, 3])
    print(tl)
    print(tl.a)

    TestList2 = namedlist("TestList2", ['d','e','f'])
    print(TestList2)
    print(TestList2.__name__)
    tl2 = TestList2([4, 5, 6])
    print(tl2)
    print(tl2.d)

    tl2.d = 3
    print(tl2.d)

    tl2_ = TestList2()
    print(tl2_)
    tl2_.d = 2
    print(tl2_.d)
