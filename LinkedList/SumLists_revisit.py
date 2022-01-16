'''
****Need to revisit****

You have two numbers represented by a linked list, where each node contains a single
digit.The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input:(7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.

Reversed one:
TC-O(N)
SC-O(N)

According to some hints in the book, I think she suggests to use recursion (the interview may ask you not to convert the list values to numbers).
'''

from LinkedList.LinkedList import LinkedList, Node


#first let us do the easier one. Digits in forward order.
def retreive_digits(LinkedList):
    head=LinkedList.head
    str_num=""
    while head is not None:
        str_num+=str(head.value)
        head=head.next
    return int(str_num)


#pass the lists and sum them up

#let's do the reverse one now

#we might need stack based implementation (LIFO)
def list_digits(LinkedList):
    head=LinkedList.head
    lst_num=[]
    while head is not None:
        lst_num.append(head.value)
        head=head.next
    return(''.join(str(num) for num in reversed(lst_num)))   #reversed returns a pointer at the end of the string


def add_numbers(l1,l2):
    return (int(list_digits(l1))+int(list_digits(l2)))


#def easier_way(l1,l2):



sll=LinkedList()
sll.appendToTail(Node(1))
sll.appendToTail(Node(9))
sll.appendToTail(Node(2))
sll.appendToTail(Node(2))

sll1=LinkedList()
sll1.appendToTail(Node(1))
sll1.appendToTail(Node(7))
sll1.appendToTail(Node(7))
sll1.appendToTail(Node(2))

print(add_numbers(sll,sll1))
