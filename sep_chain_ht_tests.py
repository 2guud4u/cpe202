import unittest
import sep_chain_ht

class MyTestCase(unittest.TestCase):
    def test_something(self):
        hashy = sep_chain_ht.MyHashTable()
        hashy.insert(2, 'nice')#test insert
        hashy.insert(3, 'noise')
        hashy.insert(8, 'noiceee')
        hashy.insert(24, 'nicely')# test collision
        self.assertEqual(hashy.collisions(), 1)
        self.assertEqual(hashy.size(), 4)
        hashy.insert(8, 'sey')#test duplicate
        print(hashy.hash)
        hashy.insert(6, 'noicey')
        hashy.insert(9, 'teeheee')
        hashy.insert(83565656565, 'haha')# test resize
        print(hashy.hash)
        self.assertEqual(hashy.get(8), (8, 'sey')) #test get()
        self.assertEqual(hashy.remove(2), (2, 'nice'))#test remove()
        self.assertAlmostEqual(hashy.load_factor(), .6363636363)# test load factor
        self.assertEqual(hashy.size(), 7)
        print(hashy.hash)


if __name__ == '__main__':
    unittest.main()
