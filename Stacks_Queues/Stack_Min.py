'''
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time

here we can use two stacks, both have the same number of elements always.
One is the normal stack, the other is the min element stack.
So at a given time, the top most element of the min stack(nim_Stack[-1]) holds the minimun element in the stack
So we can return the minimum element in O(1)

AS:O(N)    #for the additional min_Stack

'''
import math
class Stack_min():
    def __init__(self,capacity):
        self.capacity = capacity
        self.stack = list()
        self.min_stack = list()

    def push(self, item):
        if len(self.stack)==self.capacity:
            print("Min stack is full")
            return
        elif len(self.stack)==0:    #first element to be pushed
            self.min_stack.append(item)
        else:
            self.min_stack.append(min(self.min_stack[-1],item)) #append to the min
            #stack the minimum of the item and the last appended item
        self.stack.append(item)

    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty")
        else:
            self.min_stack.pop()
            print("The popped element is ",self.stack.pop())

    def min(self):
        return self.min_stack[-1]

    def print_stack(self):
        for item in self.stack:
            print(item)
        print("***End of stack***")
        for item in self.min_stack:
            print(item)
        print("End of min stack")

'''
stk=Stack_min(5)
stk.push(1)
stk.push(-2)
stk.push(-3)
stk.push(5)
stk.print_stack()
print(stk.min())

Python - Stack_Min.py:45
1
-2
-3
5
***End of stack***
1
-2
-3
-3
End of min stack
-3
'''
