import unittest
import Lab4
# how do i even test things
class MyTestCase(unittest.TestCase):
    def test_Tree(self):
        tree = Lab4.BinarySearchTree()
        tree.insert(12)
        tree.insert(5)
        tree.insert(3)
        tree.insert(1)
        tree.insert(7)
        tree.insert(9)
        tree.insert(8)
        tree.insert(11)
        tree.insert(14)
        tree.insert(13)
        tree.insert(17)
        tree.insert(20)
        tree.insert(18)
        tree.insert(13.1)
        tree.insert(12.1)
        tree.delete(8)
        self.assertEqual(tree.find(8), False)
        tree.delete(12)
        self.assertEqual(tree.find(12), False)
        self.assertEqual(tree.is_empty(), False)
        self.assertEqual(tree.find_max(), 20)
        self.assertEqual(tree.find_min(), 1)
        tree.print_tree()
        tree.print_levels()


if __name__ == '__main__':
    unittest.main()
