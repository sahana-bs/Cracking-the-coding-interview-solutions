'''
credits: https://www.openbookproject.net/thinkcs/python/english2e/ch21.html

Implementation of a tree and different types of traversal
Inorder: In-order traversal means to "visit" (often, print) the left branch, then the current node, and finally, the right
branch
Preorder:Root is visited first, then left and right. Best remembered for prefix
Postorder: Root is visited last, postfix
'''

class Tree():
    def __init__(self, data, left=None, right=None):
        self.left=left
        self.data=data
        self.right=right

    # def __str__(self):
    #     return str(self.data)

def in_order(tree):
    if tree==None:
        return
    in_order(tree.left)
    print(tree.data, end=', ' )
    in_order(tree.right)

def pre_order(tree):
    if tree==None:
        return
    print(tree.data, end=', ' )
    pre_order(tree.left)
    pre_order(tree.right)

def post_order(tree):
    if tree==None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.data, end=', ' )

'''
In_tree=Tree(12, Tree(10, Tree(5), Tree(11)),Tree(20, Tree(18),Tree(21)))
in_order(In_tree)
pre_order(In_tree)
post_order(In_tree)
#5, 10, 11, 12, 18, 20, 21,
#12, 10, 5, 11, 20, 18, 21,
# 5, 11, 10, 18, 21, 20, 12,
'''
