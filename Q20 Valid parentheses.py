"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        d={"}":"{",")":"(","]":"["}
        l=[]
        for i in s:
            if i in d.values():
                l.append(i)
            elif l and l[-1]==d[i]:
                l.pop()
            else:
                return False
        if len(l)==0:
            return True
        else:
            return False