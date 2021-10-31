import unittest
import lab6a

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test = lab6a.sorts()
        test.test(1000)
        test.test(2000)
        test.test(4000)
        test.test(8000)
        test.test(16000)
        test.test(32000)
if __name__ == '__main__':
    unittest.main()
