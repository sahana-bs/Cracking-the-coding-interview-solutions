'''
Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
of n pairs of parentheses.
EXAMPLE
Input: 3
Output: ( (() ) ) , (() ()) , (()) (), () (()) , ()() ()

Time Complexity O(2^N)


In this folder is a picture of the stack tree of this function when n=3:
So we can understand it like this:
At every level of the tree, either '(' or ')' is added to the string.
All the left branches are where ( is added, right ) is added
We know that at every point, the number of left parantheses>=number of right parantheses, hence we make this the base condition/stopping condition
Thus the maximum levels is pairs*2
The max leaf nodes is 2^n

'''
#https://algorithms.tutorialhorizon.com/generate-all-valid-parenthesis-strings-of-length-2n-of-given-n/
#pairs*2 is the length of the target string
def paren(open,close,string,pairs):
    if len(string)==pairs*2:    #base case
        print(string)
    if open>close:
       return
    if open:
        paren(open-1,close,string+"(",pairs)
    if close:
        paren(open,close-1,string+")",pairs)

pairs=3
open,close=pairs,pairs
paren(open,close,"",pairs)
