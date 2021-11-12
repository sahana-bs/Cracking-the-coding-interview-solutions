'''
Write a method to compute all permutations of a string of unique
characters.
The number of permutations of n character string is n!

TC: So the funstion permutation is called N times, so O(N). But for each call of the permutation function, maximum times it is called is N
(This is can upperbound) again. So, the total time complexity is O(N^2)
'''
#python itertools
from itertools import permutations

def perm_builtin(str):
    s=list(permutations(str))
    s=[''.join(p) for p in s]
    print(s)

#https://www.delftstack.com/howto/python/permutations-of-a-string-python/
# def permutation(index,string,n):
#     if index==n:
#         print(''.join(string))
#     else:
#         for i in range(index,n):
#             string[index], string[i]=string[i], string[index]
#             permutation(index+1,string,n)
#             string[index], string[i]=string[i], string[index]

#Python implementation of the solution as given in the book

#this is not working, need ot check on this!!
def permutation(str):
    if str=="":
        return ""
    perm=[]
    if len(str)==0:
        perm.append(" ")
        return perm
    a=str[0]
    sub=str[1:]
    words=permutation(sub)
    print(words)
    for word in words:
        for i in range(len(word)):
            s=insertAt(word,a,i)
            perm.append(s)
    return perm

def insertAt(word,c,i):
    return word[0:i]+c+word[i:]

def perm_init(str):
    s=str.upper()
    s=list(set(s))   #remove duplicates
    print(permutation(s,))

perm_init("abc")
