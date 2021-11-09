'''
Power Set: Write a method to return all subsets of a set.

Now this is an important problem. This is the idea behind other problems like max sum subarray (with consecutive or non-consecutive elements).

iterative solution:

Recursion:
TC: O(N*2^N)
credit:https://medium.com/outco/how-to-solve-power-set-c8ef7d1382ee
https://www.delftstack.com/howto/python/powerset-python/#:~:text=Use%20the%20Recursive%20Method%20to%20Find%20a%20Powerset,set%20of%20lists%2C%20sets%2C%20strings%2C%20etc.%2C%20in%20Python.
https://www.technomancy.org/python/powerset-generator-python/#:~:text=The%20powerset%20of%20a%20set%20is%20the%20set,that%20you%20can%20generate%20as%20you%20go%20along.
'''
#a power set includes an empty set, single element set and the entire array as well!

#This is literally the iterative solution
#return to this after bit maipulation

#recursive solution
def power_set_rec(index,arr,subset):
        if index==len(arr):
            print(subset)
            return
        power_set_rec(index+1,arr,subset+arr[index])
        power_set_rec(index+1,arr,subset)
        return


print(power_set_rec(0,["a","b","c"],""))
