/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// Time Complexity: O(nlogn) on average, but O(n) in the worst case of a
//                  degenerate tree (similar to a linked list)
// Space Complexity: O(n) since in the worst case we store the entire recursion
//                   stack at every node.

// Basic recursive solution
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) {
            TreeNode* node = new TreeNode(val);
            return node;
        }

        if (val < root->val) {
            root->left = insertIntoBST(root->left, val);
        }
        else {
            root->right = insertIntoBST(root->right, val);
        }
        return root;
    }
};


// Iterative solution
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) {
            TreeNode* node = new TreeNode(val);
            return node;
        }

        TreeNode* curr = root;
        TreeNode* node = new TreeNode(val);
        while (curr) {
            if (val < curr->val) {
                if (curr->left) {
                    curr = curr->left;
                }
                else {
                    curr->left = node;
                    break;
                }
            }
            else {
                if (curr->right) {
                    curr = curr->right;
                }
                else {
                    curr->right = node;
                    break;
                }
            }
        }
        return root ? root : node;
    }
};


// funky iterative solution with double pointer
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) {
            TreeNode* node = new TreeNode(val);
            return node;
        }

        TreeNode** curr = &root;

        while (*curr) {
            if (val < (*curr)->val) {
                curr = &(*curr)->left;
            }
            else {
               curr = &(*curr)->right;
            }
        }

        *curr = new TreeNode(val);
        return root;
    }
};