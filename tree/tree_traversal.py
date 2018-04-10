class TreeNode:
    def __init__(self,x):
        self.value = x
        self.right = None
        self.left = None

def CreateTree(root):
    element = input("please input number:")
    if element == "#":
        return
    else:
        root=TreeNode(element)
        root.left=CreateTree(root.left)
        root.right=CreateTree(root.right)
    return root

def pre_order(root):
    if root:
        print(root.value)
        pre_order(root.left)
        pre_order(root.right)

def mid_order(root):
    if root:
        mid_order(root.left)
        print(root.value)
        mid_order(root.right)

root = TreeNode(4)
root = CreateTree(root)
print(mid_order(root))
