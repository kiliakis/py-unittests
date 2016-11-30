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

if __name__ == '__main__':
    unittest.main()
