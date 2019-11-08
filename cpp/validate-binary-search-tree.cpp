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
    bool isValidBST(TreeNode* root) {
        return helper(root, LONG_MIN, LONG_MAX);
    }

private:
    bool helper(TreeNode* node, long lower, long upper) {
        if (!node) {
            return true;
        }

        long val = node->val;
        if (val <= lower or val >= upper) {
            return false;
        }

        if (!helper(node->right, val, upper) or !helper(node->left, lower, val)) {
            return false;
        }
        return true;
    }
};