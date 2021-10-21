'''
Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input:
Output:
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
hint::
remember shifing and swapping in a linked list does not make sense. If such a case arises, create seperate ll and merge them.

PS:
-first need to clarify if it's a single or double linked list.

1.traverse the ll
2.maintain two ll, if the node.value is <partiiton_val: append to one ll
3. else >partition_val, append to another ll
4.if it's equal, count it,
5.append count number of nodes to left and merge right with it



complexities:
TC:O(N)
AS:O(N)


'''
from LinkedList import LinkedList,Node

def Partition(ll,partition_val):
    count=0
    node=ll.head
    left=LinkedList()
    right=LinkedList()
    while node is not None:
        if node.value<partition_val:
            left.appendToTail(Node(node.value))
        elif node.value>partition_val:
            right.appendToTail(Node(node.value))
        else:
            count+=1    #gives the number of elements equal to the partition val
        node=node.next


    for i in range(0,count):  left.appendToTail(Node(partition_val))
    print("left partition")
    left.print_ll()
    print("Right partition")
    right.print_ll()

    #merge the ll
    left.merge_ll(right)
    print("after merging")
    left.print_ll()


'''
sll=LinkedList()
sll.appendToTail(Node(3))
sll.appendToTail(Node(5))
sll.appendToTail(Node(8))
sll.appendToTail(Node(5))
sll.appendToTail(Node(10))
sll.appendToTail(Node(2))
sll.appendToTail(Node(1))
Partition(sll,5)

After merging this gives: 3->2->1->5->5->8->10
'''
