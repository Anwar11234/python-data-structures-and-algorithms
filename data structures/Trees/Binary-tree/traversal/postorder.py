# algorithm:
# for each node:
# 1 - traverse the left subtree
# 2 - traverse the right subtree
# 3 - visit the node

def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.getRootVal())