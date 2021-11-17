'''
A min-heap is a complete binary tree (that is, totally filled other than the rightmost elements on the last
level) where each node is smaller than its children. The root, therefore, is the minimum element in the tree.

Two operations:
insert TC: O(log n)
extract_min

This is incomplete.
'''
import math
class MinHeap:
    def __init__(self):
        self.heap=[]  #assume an unlimited heap
        self.heap[0]=-math.inf

    def swap(self,pos1,pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos2]

    #insert an elemnent to the min heap
    def insert(self,element):
        self.heap[-1]=element
        #check if this element is smaller than it's parent
        k=len(self.heap)-1
        while self.heap[k]<self.heap[k//2]:
            swap(k,k//2)
            k=k//2

    def extract_min(self):
        print(self.heap[0])  #return the root


    #TODO heapify()
