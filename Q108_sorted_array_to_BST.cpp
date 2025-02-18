#include <bits/stdc++.h>
using namespace std;

/*
108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
*/

//  Definition for a binary tree node.
struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode *insert(struct TreeNode *root, int nums[], int low, int high)
{
    int mid = (high + low) / 2;
    if (low > high)
    {
        return NULL;
    }
    if (root == NULL)
    {
        root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
        root->val = nums[mid];
        root->left = NULL;
        root->right = NULL;
    }
    root->left = insert(root->left, nums, low, mid - 1);
    root->right = insert(root->right, nums, mid + 1, high);
    return root;
}
struct TreeNode *sortedArrayToBST(int *nums, int numsSize)
{
    struct TreeNode *root = NULL;
    root = insert(root, nums, 0, numsSize - 1);
    return root;
}