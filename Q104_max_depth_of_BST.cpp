/*
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
*/

#include<bits/stdc++.h>
using namespace std;
// Definition for a binary tree node.
struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int max(int a, int b)
{
    if (a > b)
    {
        return a;
    }
    else
    {
        return b;
    }
}
int height(struct TreeNode *root)
{
    if (root == NULL)
    {
        return 0;
    }
    else
    {
        int h1 = height(root->right);
        int h2 = height(root->left);
        return max(h1, h2) + 1;
    }
}
int maxDepth(struct TreeNode *root)
{
    int h = height(root);
    return h;
}