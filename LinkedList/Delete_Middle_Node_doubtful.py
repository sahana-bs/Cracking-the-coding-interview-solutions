'''
Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks likea->b->d->e->f


Implementation:
-Here we will use the same runner technique, one pointer is is behind another pointer by 2 nodes. If we need to
delete the node exactly in the middle, we need to know the total number of nodes. Assuming that is not
necessary(as mentioned in the problem anyway), we delete the node right after the head and before the lst

TC:O(1)
SC:O(1)

Hint #72
Picture the list 1->5->9->12. Removing 9 would make it look like 1->5->12.You only
have access to the 9 node. Can you make it look like the correct answer?

I think this means you are passed a node, need to check if it is the head or the last element if no delete it??
But how to connect nide 5's next to node12...???
'''

from LinkedList.LinkedList import LinkedList, Node

def two_pointer(LinkedList):
    #edge cases
    node=LinkedList.head
    if node.next is None:
        print("No nodes to delete")
        quit()
    elif node.next.next is None:
        print("Cannot delete the first or last node")
        quit()
    else:
        #so the lll has atleast three nodes
        runner=LinkedList.head
        print("Node deleted is ",runner.next.value)
        runner.next=runner.next.next #delete the node next to head

#
# sll=LinkedList()
# sll.appendToTail(Node(10))
# sll.appendToTail(Node(10))
# sll.appendToTail(Node(20))
# sll.appendToTail(Node(20))
# sll.appendToTail(Node(30))
# two_pointer(sll)
# sll.print_ll()
