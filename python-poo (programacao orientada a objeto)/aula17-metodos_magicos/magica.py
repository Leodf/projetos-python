"""
https://rszalski.github.io/magicmethods/
"""

class A:
    """
    def __new__(cls, *args, **kwargs):
        # print('Eu sou o new')
        # return object.__new__(cls)
        pass
    """
    def __init__(self):
        # print('Eu sou o INIT')
        pass

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)

a = A()
a(1,2,3,4,5,6, nome='Leonardo')