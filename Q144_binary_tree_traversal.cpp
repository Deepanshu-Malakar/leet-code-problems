// Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

// Example 1:

// Input: root = [1,null,2,3]

// Output: [1,2,3]

// Explanation:



// Example 2:

// Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

// Output: [1,2,4,5,6,7,3,8,9]

// Explanation:



// Example 3:

// Input: root = []

// Output: []

// Example 4:

// Input: root = [1]

// Output: [1]


#include<bits/stdc++.h>
using namespace std;


// Definition for a binary tree node.
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void preorder(TreeNode* root,vector<int> &a){
        if(root == NULL){
            return;
        }
        a.push_back(root->val);
        preorder(root->left,a);
        preorder(root->right,a);
    }
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> a;
        preorder(root,a);
        return a;
    }
};