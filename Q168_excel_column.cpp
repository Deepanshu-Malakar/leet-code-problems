// Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

// For example:

// A -> 1
// B -> 2
// C -> 3
// ...
// Z -> 26
// AA -> 27
// AB -> 28 
// ...
 

// Example 1:

// Input: columnNumber = 1
// Output: "A"
// Example 2:

// Input: columnNumber = 28
// Output: "AB"
// Example 3:

// Input: columnNumber = 701
// Output: "ZY"

#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string convertToTitle(int columnNumber) {
        int n = columnNumber;
        string s = "";
        while (n>0){
            int last = n%26;
            n = n/26;
            char x = 'A'+last-1;
            if(last == 0) {
                x = 'Z';
                n = n-1;
            }
            s = x+s;
        }
        return s;
    }
};