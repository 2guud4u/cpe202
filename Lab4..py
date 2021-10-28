class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.data = None # let key have key and level

class BinarySearchTree:
# write the __init__() method here. The tree has at least a ‘root’ node.
    def __init__(self):
        self.root = None
        self.num_item = 0
        self.target = None
    def find(self, key):# returns True if key is in a node of the tree, else False
        node = self.root
        while True:
            if key > node.key and key != node.key:
                if node.right == None:
                    return False
                node = node.right
            elif key < node.key and key != node.key:
                if node.left == None:
                    return False
                node = node.left
            else:
                print(node.key, 'is', key )
                return True

    def find_min(self): # returns min value in the tree
        self.target = self.root
        while self.target.left != None:
            self.target = self.target.left
        return self.target.key

    def find_max(self): # returns max value in the tree
        self.target = self.root
        while self.target.right != None:
            self.target = self.target.right
        return self.target.key

    def insert(self, newkey): # inserts a node with key into the correct position if not a duplicate.
        new_node = TreeNode(newkey)
        if self.root == None:
            self.root = new_node
            self.num_item += 1
            return
        self.target = self.root
        self.num_item += 1
        while True:
            if new_node.key >= self.target.key:
                if self.target.right == None:
                    self.target.right = new_node
                    return
                else:
                    self.target = self.target.right
            if new_node.key < self.target.key:
                if self.target.left == None:
                    self.target.left = new_node

                    return
                else:
                    self.target = self.target.left

    def delete(self, root, key): # deletes the node containing key, assumes such a node exists

        parent = None
        curr = root
        while curr and curr.key != key:
            parent = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        if curr is None:
            return root
        if curr.left is None and curr.right is None:
            if curr != root:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None
            else:
                root = None
        elif curr.left and curr.right:
            successor = self.delete_helper(curr.right)
            val = successor.key
            self.delete(root, successor.key)
            curr.key = val
        else:
            if curr.left:
                child = curr.left
            else:
                child = curr.right
            if curr != root:
                if curr == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                root = child
        return root
    def delete_helper(self, curr):

        while curr.left:
            curr = curr.left

        return curr

    def print_tree(self): # print inorder the entire tree
        self.inorder_print_tree(self.root)
    def is_empty(self): # returns True if tree is empty, else False
        return self.num_item == 0

    def inorder_print_tree(self, root): # print inorder the subtree of self
        if root:
            self.inorder_print_tree(root.left)
            print(root.key)
            self.inorder_print_tree(root.right)
    def print_levels(self): # inorder traversal prints list of pairs, [key, level of the node] where root is level 0
        self.print_levels_helper(self.root, 0)
    def print_levels_helper(self, root):# change to use Queues
        self.target = root


tree = BinarySearchTree()
tree.insert(5)
tree.insert(8)
tree.insert(6)
tree.insert(1)
tree.insert(4)
tree.insert(3)
tree.insert(9)
tree.insert(7)
tree.insert(8.1)
tree.insert(10)
tree.delete(5, 9)
tree.print_tree()