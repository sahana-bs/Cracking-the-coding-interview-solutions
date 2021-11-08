'''
Power Set: Write a method to return all subsets of a set.

Now this is an important problem. This is the idea behind other problems like max sum subarray (with consecutive or non-consecutive elements).

iterative solution:

Recursion:
TC: O(N*2^N)
credit:https://medium.com/outco/how-to-solve-power-set-c8ef7d1382ee
https://www.technomancy.org/python/powerset-generator-python/#:~:text=The%20powerset%20of%20a%20set%20is%20the%20set,that%20you%20can%20generate%20as%20you%20go%20along.
'''
#a power set includes an empty set, single element set and the entire array as well!

#This is literally the iterative solution
#return to this after bit maipulation

#recursive solution
def power_set(arr):
    all_subsets=[]
    def power_set_rec(index,subset):
        if index==len(arr):
            all_subsets.append([subset])
            return
        power_set_rec(index+1,subset)
        power_set_rec(index+1,subset.append(arr[index]))
    power_set_rec(0,[1,2,3])
    return all_subsets


print(power_set([1,2,3]))
