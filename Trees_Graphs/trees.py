'''
credits: https://www.openbookproject.net/thinkcs/python/english2e/ch21.html

Implementation of a tree and different types of traversal
'''

class Tree():
    def __init__(self, data, left=None, right=None):
        self.left=left
        self.data=data
        self.right=right

    def __str__(self):
        return str(self.data)

    def in_order(Self):
