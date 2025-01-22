# Binary tree node
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# In-order traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val),
        inorder(root.right)
