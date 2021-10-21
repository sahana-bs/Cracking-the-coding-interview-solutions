'''
For every recursive function:
-Determine the base case
-Computation to do
-Call the function recursively
'''


list_num=[1,2,3,5,6,7]
def getsum(num):
    if len(num)==0:     #every recursive function should have a base case
        return 0
    else:
        return (num[0]+getsum(num[1:]))   #this is where sum is computer and the function is recursively called

#print(getsum(list_num))
