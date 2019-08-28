/*
Given the root of a binary search tree with distinct values, modify it so that
every node has a new value equal to the sum of the values of the original tree
that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Note:
The number of nodes in the tree is between 1 and 100.
Each node will have value between 0 and 100.
The given tree is a binary search tree.
*/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        int accumulated_sum = 0;
        recursive_helper(root, accumulated_sum);
        return root;
    }

    void recursive_helper(TreeNode* node, int& accumulated_sum) {
        if (!node) { return ; }
        recursive_helper(node->right, accumulated_sum);
        node->val += accumulated_sum;
        accumulated_sum = node->val;

        recursive_helper(node->left, accumulated_sum);
    }
};

// Iterative solution
class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        if (root == nullptr) { return root; }

        int accumulated_sum = 0;
        vector<TreeNode*> res;
        TreeNode* curr = root;

        while (curr or res.size() > 0) {
            while (curr) {
                res.push_back(curr);
                curr = curr->right;
            }
            curr = res.back();
            res.pop_back();

            curr->val += accumulated_sum;
            accumulated_sum = curr->val;
            curr = curr->left;
        }

        return root;
    }
};


// Recursive helper function
class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        if (root == nullptr) { return root; }

        int accumulated_sum = helper_bstToGst(root, 0);
        return root;
    }

    int helper_bstToGst(TreeNode* node, int prev) {
        int acc_val = 0;
        if (node->right) {
            int increased_by = helper_bstToGst(node->right, prev);
            node->val += increased_by;
            acc_val = node->val;
        }
        else if ( !(node->right) ) {
            node->val += prev;
            acc_val = node->val;
        }

        if (node->left) {
            acc_val = helper_bstToGst(node->left, node->val);
        }
        return acc_val;
    }
};