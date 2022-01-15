class A():
    def __init__(self, par1, par2):
        self.par1 = par1
        self.par2 = par2

    def ret_par1(self):
        return self.par1

class B(A):
    #do not def init, it overrides the super class unless you want different parameter
    def ret_par2(self):
        return self.par2

A_obj = A(2,3)
# print(A_obj.ret_par1())

B_obj = B(3,4)
# print(B_obj.ret_par2())

#an interesting example from stackoverflow, @Konstantin
class A:
    def __prop_a(self):
        return 1
    def prop_b(self):
        return 10 * self.__prop_a()

class B(A):
    def __prop_a(self):
        return 2

print(B().prop_b())
print(A().prop_b())

'''
o/p:
2
4
'''
