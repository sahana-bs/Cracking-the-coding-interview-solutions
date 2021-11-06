'''
 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.

or in other words, detect if the linked list has a loop. Apparently a very favorite interview question.

DEFINITION
Circular linked list:A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C

PC:

#Hash table
 -An obvious implementation is the hash table.
 TC:(N)
 AS:(N) #dict


#the solution in the book uses two pointers, one behind the other by a step.
As we traverse the ll, we move the pointers, if they collide, the ll is a circular list and we returnt the collision point(loop element)
'''
from LinkedList.LinkedList import LinkedList,Node

def hash_table(ll):
    ht=dict()
    node=ll.head
    while node is not None:
        if node.value in ht:    #that element is already encountered
            if node.next in ht[node.value]:    #since ht[node.value] could be a list of references
                print("Collision point ",node.value)
                return True
            else:
                ht[node.value].append(node.next)
        else:
            ht[node.value]=node.next
    return False
