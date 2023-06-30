from .func1 import Func1

# 为啥下面也可以？
# from . import Func1
class Func2(object):
    @staticmethod
    def num2(x):
        return Func1.num(x)
