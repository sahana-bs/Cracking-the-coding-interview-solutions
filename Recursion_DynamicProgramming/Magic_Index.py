'''
Magic Index: A magic index in an array A [ 0••• n -1] is defined to be an index such that A[ i] =
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?


The iterative soultion of this is very easy. Let's try using recursion for this

***As soon as you see, "SORTED ARRAY", the first thing that should come to the mind is "BINARY SEARCHING"
'''
# def magic(lst):
#     if index==lst[0]:
#         return index
#     index+=1
#     return (magic(lst[1:]))
# lst=[1,4,2,5,5,7]
# print(magic(lst))

def magic(lst):
    return magic_bin(lst, 0, len(lst)-1)

def magic_bin(lst, start, end):
    if end < start:
        return -1
    mid=(start+end)//2
    if lst[mid]==mid:
        return mid
    elif lst[mid]>mid:
        magic_bin(lst,start,mid-1)
    else:
        magic_bin(lst,mid+1,end)
