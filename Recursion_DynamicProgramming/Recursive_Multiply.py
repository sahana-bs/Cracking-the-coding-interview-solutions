'''
Recursive Multiply: Write a recursive function to multiply two positive integers without using the
*operator.You can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations.

TC:O(m)
'''
#adding n "m" times
def rec_mul(n,m):
    if m==1:
        return n
    return n+rec_mul(n,m-1)


#can we cache the results and make it any better?
'''
Notice that caching here does not make sense as we are making the recursive call with different parameters
everytime.
But one direction of improvement is to find the lesser number and make that number "m", since the number of
call is dependent in that.
'''
print(rec_mul(9,7))
