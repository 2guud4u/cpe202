import unittest
import Lab2


class MyTestCase(unittest.TestCase): #test empty
    def test_something(self):
        stacky = Lab2.StackLinkedList(2)
        self.assertEqual(stacky.is_empty(), True)  # add assertion here
    def test_something2(self):
        stacky2 = Lab2.StackLinkedList(2)
        stacky2.push(3)
        self.assertEqual(stacky2.is_empty(), False)
class MyTestCase2(unittest.TestCase): #test full
    def test_something(self):
        stacky = Lab2.StackLinkedList(1)
        stacky.push(3)
        self.assertEqual(stacky.is_full(), True)
    def test_something2(self):
        stacky2 = Lab2.StackLinkedList(20)
        stacky2.push(3)
        self.assertEqual(stacky2.is_full(), False)
class MyTestCase3(unittest.TestCase): #test push and peek
    def test_something(self):
        stacky = Lab2.StackLinkedList(1)
        stacky.push(3)
        self.assertEqual(stacky.peek(), 3)
    def test_something2(self):
        stacky = Lab2.StackLinkedList(1)
        stacky.push(4)
        self.assertEqual(stacky.peek(), 4)

class MyTestCase7(unittest.TestCase): #test pop
    def test_something(self):
        stacky = Lab2.StackLinkedList(5)
        stacky.push(3)
        stacky.push(5)
        stacky.push(7)
        self.assertEqual(stacky.pop().item, 7)
        self.assertEqual(stacky.pop().item, 5)
        self.assertEqual(stacky.pop().item, 3)
class MyTestCase4(unittest.TestCase): #test size
    def test_something(self):
        stacky = Lab2.StackLinkedList(5)
        stacky.push(3)
        stacky.push(5)
        self.assertEqual(stacky.size(), 2)
class MyTestCase5(unittest.TestCase): #test stack
    def test_something(self):
        stacky = Lab2.StackLinkedList(5)
        self.assertEqual(stacky.capacity, 5)
        self.assertEqual(stacky.head, None)
        self.assertEqual(stacky.num_items, 0)
if __name__ == '__main__':
    unittest.main()
