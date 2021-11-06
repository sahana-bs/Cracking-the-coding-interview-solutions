'''
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there werejust a single stack).
FOLLOW UP
ImplementafunctionpopAt ( int index) which performs apopoperationon aspecificsub-stack

for ImplementafunctionpopAt ( int index), in push() we need to iterate across every stack and check the capacity..


'''
class SetOfStacks():
    def __init__(self,capacity):
        #create a list of lists
        self.capacity=capacity    #threshold
        self.stacks=[[]]    #interesting, list(list()) didn't work

    def push(self,item):
        if self.stacks == []:   #for the very first element
            self.stacks.append([item])
            return
        #searching for any empty space in the existing stack
        for stack in range(len(self.stacks)):
            if len(self.stacks[stack])==self.capacity:
                pass
            else:
                    #this stack is not at capacity
                self.stacks[stack].append(item)
                return

        #else create a new stack and append the item
        self.stacks.append([item])
        '''
            this part is for the normal push
            # if len(self.stacks[-1])==self.capacity:   #this stack is full
            #     self.stacks.append([item])
            # else:
            #     self.stacks[-1].append(item)
        '''

    def pop(self,index):   #general pop
        return self.stacks[index].pop()

    def print_stacks(self):
        for stack in self.stacks:
            print("Stack ",stack)
        print("************")



# stk = SetOfStacks(3)
# stk.push(1)
# stk.push(1)
# stk.push(1)
# stk.print_stacks()
# stk.push(3)
# stk.push(3)
# stk.push(3)
# stk.print_stacks()
# stk.pop(1)
# stk.push(6)
# stk.print_stacks()
