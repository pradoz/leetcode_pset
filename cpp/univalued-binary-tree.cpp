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
    bool isUnivalTree(TreeNode* root) {
        if (!root) { return true; }
        int match_val = root->val;

        if (root->left) {
            if (!isUnivalTree(root->left) or root->left->val != match_val) {
                return false;
            };
        }
        if (root->right) {
            if (!isUnivalTree(root->right) or root->right->val != match_val) {
                return false;
            };
        }
        return true;
    }
};

// More formally, using dfs as a helper function
class Solution {
public:
    bool isUnivalTree(TreeNode* root) {
        int match_val = root->val;
        is_match = true;
        dfs(root, match_val);
        return is_match;
    }

    void dfs(TreeNode* curr, int match_val) {
        if (curr)
            if (curr->val != match_val)
                is_match = false;
            if (curr->left)
                dfs(curr->left, match_val);
            if (curr->right)
                dfs(curr->right, match_val);
    }
private:
    bool is_match;
};





