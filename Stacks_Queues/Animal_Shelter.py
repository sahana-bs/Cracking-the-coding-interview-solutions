'''
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the"oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linkedlist data structure.
'''
import sys
sys.path.append('C:/Users/sahan/OneDrive/Desktop')
from py_ds_implementaions.LinkedList.LinkedList import *

class Animal_Shelter():
    def __init__(self):
        self.shelter=LinkedList()

    def enqueue(self,animal):
        self.shelter.appendToTail(Node(animal))

    def dequeueAny(self):
        to_return=self.shelter.head
        if to_return.next is not None:
            self.shelter.head=to_return.next
        return to_return

    def dequeueDog(self):
        #traverse the ll till a dog is reached
        tmp=self.shelter.head
        while tmp is not None:
            if tmp.value=="Dog":
                break
            prev=tmp
            tmp=tmp.next
        if tmp.value=="Dog":
            prev.next=tmp.next
            return
        else:
            print("No dogs in the shelter, sorry!")

    def dequeueCat(self):
        #traverse the ll till a dog is reached
        tmp=self.shelter.head
        while tmp.next is not None:
            if tmp.value=="Cat":
                break
            prev=tmp
            tmp=tmp.next
        if tmp.value=="Cat":
            prev.next=tmp.next
            return
        else:
            print("No cats in the shelter, sorry!")

    def print_shelter(self):
        self.shelter.print_ll()
        return
