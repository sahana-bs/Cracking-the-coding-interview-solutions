'''
Doubly linked list(dll) implementation

Each node has two pointers (one pointing to the previous node and the other to the next) and a value

Why dll?
we can traverse the dll in reverse.
We also need not keep a track of the previous node(eg, while delecting a node)
complexities are the same (O(N)) except additional space required for another pointer

'''
class Node:
    def __init__(self,value):
        #self.node=node
        self.prev=None
        self.value=value
        self.next=None

class DLinkedList:
    def __init__(self):
        self.head=None    #creation of an empty head node in the ll

    def appendToTail(self,node):     #remember this "node" is an object of class "Node"
        if self.head is None:
            self.head=node
        else:
            tmp=self.head
            while tmp.next is not None:   #iterate to the end of the list..
                tmp=tmp.next
            node.prev=tmp
            tmp.next=node

    def print_ll(self):
        node=self.head
        while node is not None:
            print("Node value->", node.value)
            node=node.next

    def print_reverse(self):
        print("dll in reverse")
        node=self.head
        while node.next is not None:
            node=node.next
        #node now points to the last node
        #node=node.prev
        tmp=node
        while tmp is not None:
            print("Node value->", tmp.value)
            tmp=tmp.prev


    def remove_element(self, index):
        if index==0:  #remove from the head
            print("The deleted element is ",self.head.value)
            self.head=self.head.next
        else:
            tmp=self.head
            while tmp.next is not None:
                tmp=tmp.next              #note how you do not need to keep a track of the previous element
            print("The deleted element is ",tmp.value)
            tmp=tmp.prev
            tmp.next=None


dll=DLinkedList()
dll.appendToTail(Node(10))
dll.appendToTail(Node(20))
dll.appendToTail(Node(30))
dll.print_ll()
dll.print_reverse()
#remove from the head
dll.remove_element(0)
dll.print_ll()
dll.remove_element(1)   #remove from the end
dll.print_ll()
