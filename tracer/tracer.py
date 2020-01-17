'''
Module containing Tracer metaclass and associated trace decorator.
'''
from types import FunctionType
from functools import wraps
import traceback
from pprint import pprint
import sys


class Tracer(type):
    def __new__(cls, name, bases, cls_dct):
        wrapped_cls_dct = {}
        for attribute_name, attribute in cls_dct.items():
            if attribute_name != '__init__':
                wrapped_cls_dct[attribute_name] = trace(attribute) if isinstance(attribute, FunctionType) else attribute
            else:  # overwrite __init__ method to inject instance-level changes
                def injected_init(self, *args, **kwargs):
                    self._trace = []
                    self.print_trace = lambda: pprint(self._trace, indent=4, depth=3)
                    cls_dct['__init__'](self, *args, **kwargs)  # call existing __init__ after '_trace' attr is added
                wrapped_cls_dct['__init__'] = injected_init
        return super().__new__(cls, name, bases, wrapped_cls_dct)


def trace(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._trace.append((len(self._trace) + 1, method.__name__, args, kwargs))
        try:
            return method(self, *args, **kwargs)
        except:
            traceback.print_exc()
            print('\n\n -----  ERROR!  Execution failed with above traceback.  -----\nBelow is the Object\'s method call trace.')
            print(self)
            pprint(self._trace, indent=4, depth=3)
            sys.exit()
    return wrapper
