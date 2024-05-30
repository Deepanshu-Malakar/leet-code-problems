
"""

Code
Testcase
Testcase
Test Result
118. Pascal's Triangle
Solved
Easy
Topics
Companies
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        l=[[1],[1,1]]
        for row in range(2,numRows):
            r=[1]
            for col in range(1,row+1):
                try:
                    element=l[row-1][col-1]+l[row-1][col]
                except:
                    element=1
                r.append(element)
            l.append(r)
        return l