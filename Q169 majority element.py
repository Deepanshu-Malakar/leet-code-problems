# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


#this solution is based on moores algorythm

# moores algorythm
# this algorythm helps us find which element has the heighest probability to be the majority element

# 1] make 2 variables count,element ;
# 2] at first let count=0;
# 3]run a for loop from 0 to n
# 4]if count ==0 , assign element =arr[i]
# 6]if element ==a[i], count++
# 7]if element !=a[i], count--
# 8]till the end of the for loop if count<=0 then there is no majority element
# 9]if count >0 then the majority element maybe element
# 10]count the number of times element occurs in array , if it occurs more than n/2 times it is the majority element

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
    