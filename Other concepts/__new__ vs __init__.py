'''
As a noob programmer, I used to think that __init__ in python is equivalent to a constructor in other languages.
But apparently, it's know. What! Ikr!
So, I trying to understand it better.

__init__ :as the name states, used to initialise an object. Remember, the first parameter in __init__(self,)
is self which means that the object is already created.
__new__ :function used for object creation. As I understand memory is not yet allocated when __new__ is called.


'''

class sample():

    def __new__(cls):
        print("__new__() of sample called")

    def __init__(self):
        print("__init__() of sample called")
        print("***************************")


class sample1():

    def __init__(self):
        print("__init__() of sample1 called")
        print("****************************")
        #returning anything other than None throws an error


class sample2():

    def __new__(self):
        print("__new()__ of sample2 called")
        print("***************************")


print(sample())
print(sample1())
print(sample2())

'''
output

__new__() of sample called
None
__init__() of sample1 called
****************************
<__main__.sample1 object at 0x000001BA3058F910>   #memory for the object allocated
__new()__ of sample2 called
***************************
None

which means __new__ overrides __init__ if both are defined.
'''
