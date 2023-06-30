# 从module Sub_Module1的func1.py中import Func1 class
# 两个..的原因: 一个dot表示当前目录，多一个点就往前多退一层(取parent目录)
from ..Sub_Module1.func1 import Func1
class Func1(object):
    @staticmethod
    def num1(x):
        return Func1.num(x)
