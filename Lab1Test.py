import unittest
import Lab1A
import Lab1B

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertAlmostEqual(Lab1B.squareroot(4), 2)
class Test2(unittest.TestCase):
    def test_index(self):
        self.assertEqual(Lab1A.indexOf('Mississippi', 'ps', 0), -1)
if __name__ == '__main__':
    unittest.main()
