'''
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
'''
class MyQueue():
    def __init__(self):
        self.instack=list()
        self.outstack=list()

    def add(self,item):
        self.instack.append(item)

    def remove(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())    #this is where we reverse the order of elements
        return self.outstack.pop()

# q=MyQueue()
# q.add(2)
# q.add(4)
# q.add(6)
# print(q.remove())
