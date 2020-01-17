# import unittest
import sys
sys.path.insert(1, '..')
import tracer


class TestClass(metaclass=tracer.Tracer):
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        if val == 5:
            x = 1 / 0

    def subtract(self, val):
        self.value -= val



if __name__ == '__main__':
    test = TestClass()
    test2 = TestClass()

    test.add(3)
    test.subtract(2)
    test.add(4)
    test.add(8)
    test.print_trace()
    test.add(1)
    test2.add(7)
    # use below line to test error handling and trace printout
    # test.add(5)

    test2.subtract(3)
    test.print_trace()
    test2.add(1)

    test.print_trace()
    test2.print_trace()
    test.print_trace()
    test2.print_trace()
