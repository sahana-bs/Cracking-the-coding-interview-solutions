'''
Intersection: Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined based on reference, not value.
That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.

PC:
#brute force
-traverse the linked list1
    traverse the linked list2
    we need to check if node.next of one ll points to the node of the other ll
    TC:O(N*M)

#hash table sol:O(M+N)
    -traverse both the lists and store the references and compare them

#concept of intersection, solution from the book
We now have a multistep process.
1. Run through each linked list to get the lengths and the tails.
2. Compare the tails. If they are different (by reference, not by value), return immediately.There is no intersection.
3. Set two pointers to the start of each linked list.
4. On the longer linked list, advance its pointer by the difference in lengths.
5. Now, traverse on each linked list until the pointers are the same

    complexity:::
    TC:O(N)
    AS:O(1) #for tmp variables
'''
from LinkedList.LinkedList import LinkedList,Node

class Intersect():
    def __init__(self,ll1,ll2):
        self.len1=0
        self.len2=0
        self.ll1=ll1
        self.ll2=ll2

    def check_intersection_BruteForce(self):
        node1=self.ll1.head
        node2=self.ll2.head
    #to improve the performance we can check the smaller list and loop based on that??
        while node1 is not None:
            while node2 is not None:
                if node1.next == node2:   #if node1 points to node2
                    print("The intersecting node is ",node.value)
                    return True
                node2=node2.next
            node1=node1.next
            return False


    def check_intersection(self):
        node1=self.ll1.head
        node2=self.ll2.head
        while node1 is not None:
            prev1=node1
            self.len1+=1
            node1=node1.next
        while node2 is not None:
            prev2=node2
            self.len2+=1
            node2=node2.next
        if prev1.next!=prev2.next:   #both the lists should have the same tail
            return False
        if self.len1==1 and self.len2==1:  #single node cannot intersect
            return False
        return True

    def intersecting_node(self):
        node1=self.ll1.head
        node2=self.ll2.head
        if self.check_intersection():
            diff=abs(self.len2-self.len2)
            if self.len1>=self.len2:
                #advance the node1 by diff
                for i in range(0,diff):
                    node1=node1.next
            else:
                for i in range(0,diff):
                    node2=node2.next

            #now both are the same length, traverse and compare to find the intersecting node
            while node1 is not None:
                if node1!=node2:
                    node1=node1.next
                    node2=node2.next
                print("The intersecting node is ",node1.value)
                exit(1)
