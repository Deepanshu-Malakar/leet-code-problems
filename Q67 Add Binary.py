"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=str(bin(self.dec(a)+self.dec(b)))
        r=x[2:]
        return r
        pass
    def dec(self,n:str):
        s=0
        for i in range(0,len(n)):
            s+=int(n[i])*2**(len(n)-1-i)
        return s