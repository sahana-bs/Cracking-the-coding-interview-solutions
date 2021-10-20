'''
Implement a function to check if a linked list is a palindrome


PC:
1.use two pointers, one from the head and one from tail (reversed) (recursive approach, for this we need the
number of nodes information)\
2.Traverse the ll, append the elements to a list
    Traverse the list in reversed, compare every element (n/2, since length of list can be found)
    TC:O(N)
    AS:O(N)
'''
from LinkedList.LinkedList import LinkedList, Node

def return_list(ll):
    head_ptr=ll.head
    list_char=[]
    while head_ptr is not None:
        list_char.append(head_ptr.value)
        head_ptr=head_ptr.next
    return list_char

def check_palin(ll):
    list_char=return_list(ll)
    head=ll.head
    for i in range(int(len(list_char)/2)):
        if head.value!=list_char[len(list_char)-1-i]:
            return False
            exit(1)
        head=head.next
    return True

# sll=LinkedList()
# sll.appendToTail(Node(1))
# sll.appendToTail(Node(5))
# sll.appendToTail(Node(2))
# sll.appendToTail(Node(1))
# print(check_palin(sll))
