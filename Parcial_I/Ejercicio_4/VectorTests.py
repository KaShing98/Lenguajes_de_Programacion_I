import unittest
from Vector import Vector

class VectorTests(unittest.TestCase):

    def test_print(self):
        self.assertEqual(str(Vector(12, -34, 42)), "(12, -34, 42)")

    def test_eq(self):
        self.assertEqual(Vector(12, -34, 42) == 23, False)

    def test_add_vector(self):
        a = Vector(1, 12, 13)
        b = Vector(1, -10000, 0)
        self.assertEqual(a + b, Vector(2, -9988, 13))
    
    def test_add_number(self):
        a = Vector(13, -12, 60)
        self.assertEqual(a + 2, Vector(15, -10, 62))

    def test_sub_vector(self):
        a = Vector(1, 134442, -13)
        b = Vector(1, 985, 4)
        self.assertEqual(a - b, Vector(0, 133457, -17))
    
    def test_sub_number(self):
        a = Vector(3498, 45, -39)
        self.assertEqual(a - 1034, Vector(2464, -989, -1073))

    def test_mul_vector(self):
        a = Vector(7, -1, 2)
        b = Vector(1, 4, -2)
        self.assertEqual(a * b, Vector(-6, 16, 29))
    
    def test_mul_number(self):
        a = Vector(46, 78, -89)
        self.assertEqual(a * 42, Vector(1932, 3276, -3738))
        
    def test_mod_vector(self):
        a = Vector(1, 0.5, 3)
        b = Vector(4, -4, 1)
        self.assertEqual(a % b, 5)
    
    def test_mod_number(self):
        a = Vector(2334, 34, 456)
        self.assertEqual(a % 11, Vector(2, 1, 5))

if __name__ == '__main__':
    unittest.main()