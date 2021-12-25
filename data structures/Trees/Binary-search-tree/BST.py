class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size 

    def has_key(self , key):
        return self.bstSearch(self.root , key) is not None

    def valueOf(self , key):
        node = self.bstSearch(self.root , key)
        assert node is not None , "key not found"
        return node.value        

    # returns None if the tree is empty or if target isn't found
    def bstSearch(self , subtree , target):
        if subtree is None:
            return None
        elif target < subtree.key:
            return self.bstSearch(subtree.left , target)           
        elif target > subtree.key:
            return self.bstSearch(subtree.right , target)   
        else: # the current Node key == target
            return subtree        

    def BSTminimum(self , subtree):
        if subtree is None:
            return None
        else:
            if subtree.left is None:
                return subtree
            else:
               return self.BSTminimum(subtree.left)        

    def BSTmaximum(self , subtree):
        if subtree is None:
            return None
        else:
            if subtree.right is None:
                return subtree
            else:
                return self.BSTmaximum(subtree.right)

    # Adds a new entry to BST or replaces the value of an existing key.
    def add(self , key , value):
        if self.root is None: # if the tree is empty
            self.root = BSTNode(key , value)
            self.size = 1
        else:
            node = self.bstSearch(self.root , key ) # Find the node containing the key, if it exists.
            if node is not None:  # If the key is already in the tree, update its value.
                node.value = value
                return False
            else: # the key doesn’t exist in the tree, and we need to add a new entry.
                self.bstInsert(self.root , key , value)
                self.size += 1
                return True    

    # This method inserts a new item, recursively
    def bstInsert(self, subtree , key , value):
        if key < subtree.key:
            if subtree.left is None: # base case
                subtree.left = BSTNode(key , value)
            else:
                self.bstInsert(subtree.left , key , value)
        else:
            if subtree.right is None: # base case
                subtree.right = BSTNode(key , value)
            else:
                self.bstInsert(subtree.right , key , value)  

    def remove(self , key):                                          
        # Find the node to be deleted, N.
        node = self.bstSearch(self.root , key)
        assert node is not None , "Invalid key"
        self.root = self.bstRemove(self.root , key)
        self.size -= 1

    def bstRemove(self , subtree , target):
        if target < subtree.key:
            subtree.left = self.bstRemove(subtree.left , target)
            return subtree
        elif target > subtree.key:
            subtree.right = self.bstRemove(subtree.right , target)
            return subtree   
        else: # target == subtree.key      
            if subtree.left is None and subtree.right is None: # no children
                return None
            elif  subtree.left is None or subtree.right is None: # one child
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor = self.BSTminimum(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.right = self.bstRemove(subtree.right , successor.key)
                return subtree


class BSTNode:
    def __init__(self , key , value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None