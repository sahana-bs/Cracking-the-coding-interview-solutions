import sys
class Stack():
    def __init__(self,capacity):
        self.capacity = capacity
        self.top = -1
        self.stack = list()

    def push(self, item):
        if len(self.stack)==self.capacity:
            print("Stack is full")
            return
        else:
            self.stack.append(item)
            self.top+=1
            return

    def pop(self):
        if len(self.stack)==0:
            sys.exit("Stack is empty")
        else:
            print("The popped element is ",self.stack[self.top])
            self.top-=1
            return

    def peek(self):
        if self.top!=-1:
            return self.stack[self.top] 

    def is_empty(self):
        if len(self.stack)==0 or self.top==-1:
            return True
        return False

    def print_stack(self):
        if len(self.stack)==0:
            print("Stack is empty")
            return
        else:
            for i in range(0,self.top+1):
               print(self.stack[i],end=',')
            print()
