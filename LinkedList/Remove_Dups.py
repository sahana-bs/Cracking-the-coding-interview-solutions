'''
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

-No additional time or space(exceot for the new pointer) required
'''
from LinkedList import LinkedList,Node

def remove_duplicates(Linkedlist):
    node=Linkedlist.head
    while node.next is not None:
        #prev=node
        if node.value==node.next.value:
            node.next=node.next.next
            continue
        node=node.next
'''
o/p::

sll=LinkedList()
sll.appendToTail(Node(10))
sll.appendToTail(Node(10))
sll.appendToTail(Node(20))
sll.appendToTail(Node(20))
sll.appendToTail(Node(30))
sll.print_ll()
remove_duplicates(sll)
print("After duplicate removal")
sll.print_ll()
'''
