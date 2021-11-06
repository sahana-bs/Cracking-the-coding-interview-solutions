'''
 Implement an algorithm to find the kth to last element of a singly linked list

 implementation 1:
 traverse the ll to find the number of elements and then traverse it again till (count-k+1) elements
 TC:O(N)
 SC: O(1)

Hint #25
If you don't know the linked list size, can you compute it? How does this impact the
runtime?  RECURSION!!!

Hint #126
Can you do it iteratively? Imagine if you had two pointers pointing to adjacent nodes
and they were moving at the same speed through the linked list. When one hits the end
of the linked list, where will the other be?
This is interesting, let's try this

implementation 2:
TC=O(N) faster than the previous implementation
SC=O(1) additional space for the pointers
 '''

from LinkedList.LinkedList import LinkedList, Node

def returnk(LinkedList,k):
    count=0
    node=LinkedList.head
    while node is not None:
        count+=1
        node=node.next
    print("The number of nodes are ",count)
    node=LinkedList.head
    step=1
    while step<count-k:
        node=node.next
        step+=1
    print("The value in the kth to last element is ", node.value)

#here we maintain two pointers, prev is k nodes behind "node" which is the node used for traversal
def two_pointer(LinkedList, k):
    node=LinkedList.head
    count=1
    prev=LinkedList.head
    while node is not None:
        if count-1>k:
            prev=prev.next
        node=node.next
        count+=1

    print("The value in the kth to last element is ", prev.value)


# sll=LinkedList()
# sll.appendToTail(Node(10))
# sll.appendToTail(Node(10))
# sll.appendToTail(Node(20))
# sll.appendToTail(Node(20))
# sll.appendToTail(Node(30))
# two_pointer(sll,3)
