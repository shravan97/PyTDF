from PyTDF import *
import unittest

class AttrReadTest(unittest.TestCase):

    class Temp(object):
        def val(self, arg):
            return arg+123

    def test_attr_simple(self):
        # Write a new class again
        node = Node(None, None)
        proxy_object = proxy(node)
        func = proxy_object.attr

        self.assertEqual(proxy_object._cur_attr, "attr")

    def test_return_value(self):

        t = AttrReadTest.Temp()
        node = Node(None, None)
        node.value = t
        proxy_object = proxy(node)

        self.assertEqual(proxy_object.val(21), 144)