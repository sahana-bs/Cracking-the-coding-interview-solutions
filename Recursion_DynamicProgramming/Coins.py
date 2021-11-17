'''
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.

Looks similar to triple_step. But the difference between this and the triple_step is that (1,2),(2,1) is different in triple_step but
in this (1,5),(5,1) is the same.

TC(2^n)

solution inspiration: https://www.bing.com/videos/search?q=coin++change+problem+recusrison&docid=608005985880772957&
mid=485A8842A16A7CF2604A485A8842A16A7CF2604A&view=detail&FORM=VIRE
'''
def coins(n,index,change):
    if n<0:
        return 0
    if n == 0:
        return 1
    if index>=len(change):
        return 0
    return coins(n-change[index],index,change)+coins(n,index+1,change)
change=[1,5,10,25]
print(coins(10,0,change))
