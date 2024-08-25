# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 
class Solution:
    def factorial(self,n):
        self.product=1
        for i in range(1,n+1):
            self.product=self.product*i
        return self.product
    
    def ncr(self,n,r) -> int:
        a=self.factorial(n)
        b=self.factorial(n-r)
        c=self.factorial(r)
        return int(a/(b*c))
        
    def climbStairs(self, n: int) -> int:
        self.ans=0
        for b in range(0,n//2 +1):
            a=n-2*b
            self.ans+=self.ncr(a+b,b)
        return self.ans