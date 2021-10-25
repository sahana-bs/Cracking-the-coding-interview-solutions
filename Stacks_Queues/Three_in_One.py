'''
Three in One: Describe how you could use a single array to implement three stacks

#let us assume that the capacity of each stack is the same

complexities:
TC:O(1)
As:O(N)
'''

class three_in_one():
    #stack_no identifies the number of stacks and capacity is each stack's capacity
    def __init__(self,number_stacks,capacity):
        self.stack=list()
        self.capacity=capacity
        self.top=[-1 for i in range(0,self.capacity/number_stacks)]

    def push(self,stack_no,item):
        if self.top[stack_no]!=self.capacity-1:
            self.stack[(self.capacity*stack_no)+self.top[stack_no]]=item
            self.top[stack_no]+=1
            return
        print("Stack is full")
        return

    def pop(self,stack_no):
        if c==-1:
            print("Stack is empty")
            return
        else:
            print("The popped element is ",self.stack[self.top[stack_no]]
            self.top[stack_no]-=1
            return

    #similarly print and peek functions can be written
