#https://leetcode.com/problems/3sum/

class Solution:

    def threeSum(nums):
        res=[] #to store the final result
        n= len(nums)
        if n<3:
            return []   #cannot form any triplets

        nums.sort()
        print(nums)
        #let's use the two pointer approach

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:    #skip the duplicates from left
                continue
            print("inside for", nums)
            j=i+1
            k=len(nums)-1
            while j<k:
                sum_ = nums[i]+nums[j]+nums[k]
                if sum_==0:
                #add to result
                    res.append([nums[i],nums[j],nums[k]])
                    if nums[k]==nums[k-1]:      #skip duplicates from right
                        k=k-1

                elif sum_>0:
                    k=k-1
                else:
                    j=j+1
        print(res)
        return res

sol=Solution()
print(Solution.threeSum([-1,0,1,2,-1,-4]))
