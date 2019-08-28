// merge_two_binary_trees.cpp

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// Recusive solution
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (!t1) return t2;
        if (!t2) return t1;

        t1->val += t2->val;
        t1->left = mergeTrees(t1->left, t2->left);
        t1->right = mergeTrees(t1->right, t2->right);
        return t1;
    }
};

// Helper function solution
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (!t1) return t2;
        if (!t2) return t1;

        t1->val += t2->val;
        merge(t1, t2);

        return t1;

    }
    void merge(TreeNode* t1, TreeNode* t2) {
        if (t1->left and t2->left) {
            t1->left->val += t2->left->val;
            merge(t1->left, t2->left);
        } else if (t2->left) {
            t1->left = t2->left;
        }

        if (t1->right and t2->right) {
            t1->right->val += t2->right->val;
            merge(t1->right, t2->right);
        } else if (t2->right) {
            t1->right = t2->right;
        }
    }
};

// Iterative? solution
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (!t1) return t2;
        if (!t2) return t1;

        void merge(TreeNode* t1, TreeNode* t2) {
            if (t1->left and t2->left) {
                t1->left->val += t2->left->val
                merge(t1->left, t2->left)
            }
            if (t1->right and t2->right) {
                t1->right->val += t2->right->val
                merge(t1->right, t2->right)
            }

        }

        return t1;
    }
};

