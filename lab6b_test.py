import unittest
import lab6b

class MyTestCase(unittest.TestCase):
    def test_something(self):# for sort first random
        print('random first')
        test = lab6b.quicksorty_first()
        test.test(100)
        test.test(200)
        test.test(400)
        test.test(800)
    def test_something2(self):# for sort median random
        print('random median')
        test = lab6b.quickysort_median()
        test.test(100)
        test.test(200)
        test.test(400)
        test.test(800)
    def test_something3(self):# for sort first ordered
        print('ordered first')
        test = lab6b.quickysort_first_random()
        test.test(100)
        test.test(200)
        test.test(400)
        test.test(800)
    def test_something4(self):# for sort median ordered
        print('ordered median')
        test = lab6b.quickysort_median_random()
        test.test(100)
        test.test(200)
        test.test(400)
        test.test(800)
if __name__ == '__main__':
    unittest.main()
