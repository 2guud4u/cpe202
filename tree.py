import treequeue


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

    def delete(self, key): # deletes the node containing key, assumes such a node exists
        self.num_item -= 1
        node = self.root
        old_node = None
        shifter_node = None
        shifter_node2 = None
        case = None
        case2 = None
        while True: # find the key for deletion
            if key > node.key and key != node.key: # to the right
                old_node = node
                node = node.right
                case = 0
            elif key < node.key and key != node.key: # to the left
                old_node = node
                node = node.left
                case = 1 # for if the right of node has no child
            else:

            #case no children
                if node.right == None and node.left == None:
                    if node != self.root:
                        if case == 0:
                            old_node.right = None
                        if case == 1:
                            old_node.left = None
                        break
                    else:
                        self.root = None
                    break
            #case 2 children
                if node.right != None and node.left != None:
                    shifter_node = node.right
                    while shifter_node.left != None:
                        shifter_node2 = shifter_node
                        shifter_node = shifter_node.left
                        case2 = 1

                    if node != self.root: #replace node
                        if case == 0:
                            old_node.right = shifter_node
                            if case2 == 1:
                                shifter_node2.left = None
                                shifter_node.right = node.right
                            shifter_node.left = node.left
                            break
                        if case == 1:

                            old_node.left = shifter_node
                            if case2 == 1:
                                shifter_node2.left = None
                                shifter_node.right = node.right
                            shifter_node.left = node.left
                            break
                    else:

                        shifter_node.left = self.root.left
                        if shifter_node.right != None:
                            shifter_node2.left = shifter_node.right
                        else:
                            shifter_node2.left = None
                        shifter_node.right = self.root.right
                        self.root = shifter_node
                        break
                #case 1 child
                else:

                    if node.right != None:
                        shifter_node = node.right
                        if case == 0:
                            old_node.right = shifter_node
                        if case == 1:
                            old_node.left = shifter_node

                        break
                    else:

                        shifter_node = node.left
                        if case == 0:
                            old_node.right = shifter_node
                        if case == 1:
                            old_node.left = shifter_node
                        break

    def print_tree(self): # print inorder the entire tree
        self.inorder_print_tree(self.root)
    def is_empty(self): # returns True if tree is empty, else False
        return self.num_item == 0

    def inorder_print_tree(self, root): # print inorder the subtree of self
        if root:
            self.inorder_print_tree(root.left)
            print(root.key)
            self.inorder_print_tree(root.right)


    def print_levels(self):  # inorder traversal prints list of pairs, [key, level of the node] where root is level 0
        queuey = Lab4Queue.QueuekLinkedList(100)
        self.print_levels_helper(self.root, queuey)
    def print_levels_helper(self, root, queuey):  # change to use Queues
        if root is None:
            return
        spacer = "hehe"
        lvl = 0
        queuey.enqueue(root)
        queuey.enqueue(spacer)
        while queuey.size() > 0:
            rooty = queuey.dequeue()
            if rooty != spacer:
                if rooty != None:
                    print(rooty.key, "lvl is", lvl)
                    if root.left != None:
                        queuey.enqueue(rooty.left)
                    if root.right != None:
                        queuey.enqueue(rooty.right)
            else:
                print('____________')
                if queuey.is_empty():
                    break
                lvl += 1
                queuey.enqueue(spacer)












