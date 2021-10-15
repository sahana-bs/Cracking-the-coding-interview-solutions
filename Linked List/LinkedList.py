'''
Singly linked list(sll) implementation

ideally an element from the ll is removed from first or last, removing/inserting in the middle does not make sense
mostly because ll does not have an order(elements are not continuosly stored unlike arrays)

complexities:
TC: insertion(at the end/start/middle) O(N), deletion O(N)
SC: O(N)-to store the ll

'''
class Node:
    def __init__(self,value):
        #self.node=node
        self.value=value
        self.next=None    #recollect that python has no keyword "null"

class LinkedList:
    def __init__(self):
        self.head=None    #creation of an empty head node in the ll

    def appendToTail(self,node):     #remember this "node" is an object of class "Node"
        if self.head is None:
            self.head=node
        else:
            tmp=self.head
            while tmp.next is not None:   #iterate to the end of the list..
                tmp=tmp.next
            tmp.next=node


    def print_ll(self):
        node=self.head
        while node is not None:
            print("Node value is ", node.value)
            node=node.next

    def remove_element(self, index):
        if index==0:  #remove from the head
            print("The deleted element is ",self.head.value)
            self.head=self.head.next
        else:
            tmp=self.head
            while tmp.next is not None:
                prev=tmp
                tmp=tmp.next
            print("The deleted element is ",tmp.value)
            prev.next=None



sll=LinkedList()
sll.appendToTail(Node(10))
sll.appendToTail(Node(20))
sll.appendToTail(Node(30))
sll.print_ll()
sll.remove_element(1)   #remove from the end
sll.print_ll()
#remove from the head
sll.remove_element(0)   #remove from the end
sll.print_ll()
