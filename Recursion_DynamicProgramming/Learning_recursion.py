'''
For every recursive function:
-Determine the base case
-Computation to do
-Call the function recursively
'''
import time

list_num=[1,2,3,5,6,7]
def getsum(num):
    if len(num)==0:     #every recursive function should have a base case
        return 0
    else:
        return (num[0]+getsum(num[1:]))   #this is where sum is computer and the function is recursively called

print(getsum(list_num))

def fib_rec(n):
    if n==0: return 0
    if n==1: return 1
    return fib_rec(n-1)+fib_rec(n-2)
start_time=time.time()
print(fib_rec(20))
print("Time taken is ",time.time()-start_time)

'''
6765
Time taken is  0.0010001659393310547
'''


memo=[0,1]
def fib_dp(n):
    return fib_memo(n,memo)

def fib_memo(n,memo):
    if n<len(memo):   #value not yet calculated
        return memo[n-1]
    memo.append(fib_memo(n-1,memo)+fib_memo(n-2,memo))
    return memo[n]
start_time=time.time()
print(fib_dp(40))
print("Time taken is ",time.time()-start_time)
'''
1822473
Time taken is  0.0
'''
