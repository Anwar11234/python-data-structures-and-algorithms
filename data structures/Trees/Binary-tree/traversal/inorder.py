# algorithm:
# for each node:
# 1 - traverse the left subtree
# 2 - visit the node
# 3 - traverse the right subtree

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.getRootVal())
        inorder(root.right)