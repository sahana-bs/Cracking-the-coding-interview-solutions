'''
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.

Looks similar to triple_step. But the difference between this and the triple_step is that (1,2),(2,1) is different in triple_step but in this (1,5),(5,1)
is hte same.

'''
#this code considers a lot of duplicate solutions, need to rectify this
def coins(n):
    if n<0:
        return 0
    if n == 0:
        return 1          #there are two ways to reach if there are only two steps: 0,2 and 1,1
    return coins(n-25)+coins(n-10)+coins(n-5)+coins(n-1)
print(coins(10))
