from binarytree import build

nodes = [1,2,3,4,5,None,6,7]

binary_tree = build(nodes)

print("The binary tree is:\n",binary_tree)


'''class TreeNode:
    def __init__(self,data,left = None,right= None):
        self.data = data
        self.left_child = left
        self.right_child = right


node1 = TreeNode('B')
node2 = TreeNode('C')

tree = TreeNode('A',node1,node2)

print(tree)
'''
