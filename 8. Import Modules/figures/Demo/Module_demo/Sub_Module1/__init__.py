# 从func1.py中import Func1 class
from .func1 import Func1

# 从当前目录中import func2(.py)
from . import func2

__all__ = ["Func1",
          "func2"]
