# algorithm:
# for each node:
# 1 - visit the node
# 2 - traverse the left subtree
# 3 - traverse the right subtree

def preorder(root):
    if root != None:
        print(root.getRootVal())
        preorder(root.left)
        preorder(root.right)