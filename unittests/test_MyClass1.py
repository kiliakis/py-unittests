import unittest
from src.exampleCode1 import MyClass1


class TestMyClass1(unittest.TestCase):

    def test_constructor1(self):
        obj = MyClass1()
        self.assertEqual(obj.a, 0)
        self.assertEqual(obj.b, 1)
        self.assertEqual(obj.c, 2)

    def test_constructor2(self):
        obj = MyClass1(b=4.5, c=8)
        self.assertEqual(obj.a, 0)
        self.assertEqual(obj.b, 4.5)
        self.assertEqual(obj.c, 8)

    def test_product1(self):
        obj = MyClass1(1, 2, 3)
        self.assertEqual(obj.getProduct(), 6)

    def test_min1(self):
        obj = MyClass1(2, 2, 2)
        self.assertEqual(obj.getMin(), 2)

    def test_min2(self):
        obj = MyClass1(-10, 2, 3)
        self.assertEqual(obj.getMin(), -10)

    def test_max(self):
        obj = MyClass1(1, 2, 3)
        self.assertEqual(obj.getMax(), 3)

if __name__ == '__main__':
    unittest.main()
