import unittest
import string_checker

class MyTestCase(unittest.TestCase):
    def test_something(self):
        stacky = string_checker.StringChecker()
        self.assertEqual(stacky.isBalanced('{nice}'), True)
        self.assertEqual(stacky.isBalanced('[nice]'), True)
        self.assertEqual(stacky.isBalanced('(nice)'), True)
        self.assertEqual(stacky.isBalanced('{nice}))'), False)# d
        self.assertEqual(stacky.isBalanced('[{nice}))'), False)# d
        self.assertEqual(stacky.isBalanced('()[]{}()()()(){}{}[]'), True)# b
        self.assertEqual(stacky.isBalanced('({{({})}})'), True)  # b
        self.assertEqual(stacky.isBalanced('(([()'), False)# c
        self.assertEqual(stacky.isBalanced('[[()]'), False)  # c
        self.assertEqual(stacky.isBalanced('({)[}[]]'), False)  # e
        self.assertEqual(stacky.isBalanced('defhaisuhd'), True)# a
        self.assertEqual(stacky.isBalanced('uuhuhkb'), True) # a
        self.assertEqual(stacky.isBalanced('{(}{([)'), False)# e
        self.assertEqual(stacky.isBalanced('({)[[]}}}}'), False)# g
        self.assertEqual(stacky.isBalanced('[{][}[())))'), False)  # g

if __name__ == '__main__':
    unittest.main()
