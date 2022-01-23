#construction and insertion of nodes in bst..
#questions on bst https://medium.com/techie-delight/binary-search-tree-bst-practice-problems-and-interview-questions-ea13a6731098
#https://www.techiedelight.com/insertion-in-bst/


class Tree():
    left = right = None
    def __init__(self, data):
        self.data = data

def in_order(tree):
    if tree==None:
        return
    in_order(tree.left)
    print(tree.data, end=', ' )
    in_order(tree.right)

def insert_node(root, node):
    if root is None:
        return Tree(node)  #create a new node
    if node < root.data:
        root.left = insert_node(root.left, node)
    else:
        root.right = insert_node(root.right, node)

    return root

def constructBST(keys):
    root = None
    for key in keys:
        root = insert_node(root, key)
    return root

def delete_node(root, key):
    parent = None
    curr = root
    #search for the key
    while curr and curr.data!=key:
        #store the parent of the key
        parent = curr
        if cur









if __name__ == '__main__':

    keys = [15, 10, 20, 8, 12, 16, 25, 2]
    root = constructBST(keys)
    #print(root) root is a tree object
    in_order(root)
