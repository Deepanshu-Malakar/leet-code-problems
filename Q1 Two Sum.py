"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

class Solution:
    def twoSum(self, nums:list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i,j in nums:
        #     if i+j==target:
        #         # self.l.append(i,j)
        #         return [nums.index(i),nums.index(j)]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]    

a=Solution()
print(a.twoSum([2,7,11,15],9))

