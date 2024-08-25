# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


#this solution is based on moores algorythm
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cnt=0
        ele=nums[0]
        for i in range(0,len(nums)):
            if cnt==0:
                ele=nums[i]
                cnt=1
            elif nums[i]==ele:
                cnt+=1
            else:
                cnt-=1
        return ele
    