class Queue():
    def __init__(self, capacity):
        self.capacity=capacity
        self.queue = list()

    def add(self,item):
        if len(self.queue)==self.capacity:
            print("Queue is full")
            return
        else:
            self.queue.append(item)

    def remove(self):
        if len(self.queue)==0:
            print("Queue if empty")
            return
        else:
            print("The removed element is ",self.queue.pop(0))
            return

    def peek(self):
        if len(self.queue)==0:
            print("Queue is empty")
            return
        else:
            return self.queue[0]


    def is_empty(self):
        if len(self.queue)==0:
            return True
        return False

    def print_q(self):
        if len(self.queue)==0:
            print("Queue is empty")
            return
        else:
            for i in range(0,len(self.queue)):
                if self.queue[i]:
                    print(self.queue[i],end=',')
            print()


q=Queue(5)
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.add(5)
q.add(7)
q.print_q()
q.remove()
q.remove()
q.print_q()
print(q.peek())
