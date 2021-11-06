'''
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs

recursive approach
TC: O(3^N)
As: Stack space of N^N I think

DP
TC:O(N)

Space efficient DP:
TC:O(N)
AS:O(1)  !!
'''
def triple_step(n):
    if n == 0 or n==1:
        return 1
    if n==2:
        return 2               #there are two ways to reach if there are only two steps: 0,2 and 1,1
    return triple_step(n-3)+triple_step(n-2)+triple_step(n-1)
print(triple_step(4))

memo=[1,2]    #to cache the results
def triple_dp(n):
    return triple_dp_memo(n,memo)

def triple_dp_memo(n,memo):
    if n < len(memo):
        return memo[n-1]
    memo.append(triple_dp_memo(n-3,memo)+triple_dp_memo(n-2,memo)+triple_dp_memo(n-1,memo))
    return memo[n-1]
print(triple_dp(4))


def triple_dp_space(n):
    step_i=1    #base cases
    step_j=2
    step_k=4    #4 ways to reach the third stair 1,1,1 1,2 2,1 3
    ways=0
    if n==0 or n==1 or n==2:
        return n
    else:
        for i in range(4, n+1):
            ways = step_i + step_j + step_k
            step_i = step_j
            step_j = step_k
            step_k = ways
        return ways

print(triple_dp_space(4))
