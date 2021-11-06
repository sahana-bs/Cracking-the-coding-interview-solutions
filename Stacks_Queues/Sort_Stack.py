'''
 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array).The stack supports the following operations: push, pop, peek, andisEmpty

Assuming infinite stacks for now. So, no capacity.


This is a very brute force kinda solution
AS: O(N)

Looking at hte solution in the book, looks like this is it!
'''
class Sort_Stack():
    def __init__(self):
        self.stack=list()
        self.tmp=list()

    def push(self,item):
        if self.stack:
            count=0
            for i in range(len(self.stack)):
                if item>self.stack[i]:
                    count+=1
            for i in range(len(self.stack)-count):
                self.tmp.append(self.stack.pop())
            #now append the item
            self.stack.append(item)
            while self.tmp:
                self.stack.append(self.tmp.pop())
        else:
            self.stack.append(item)


    def pop(self):
        if not self.stack:
            return self.stack.pop()
        print("Stack is empty")

    def peek(self):
        if not self.stack:
            return self.stack[-1]

    def isEmpty(self):
        if self.stack is None:
            return True
        return False

    def prt(self):
        if self.stack:
            for item in self.stack:
                print(item, end=' ')


SortStk=Sort_Stack()
SortStk.push(5)
SortStk.push(50)
SortStk.push(9)
SortStk.push(1)
SortStk.prt()
