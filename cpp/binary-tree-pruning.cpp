/*We are given the head node root of a binary tree, where additionally every
node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing
a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a
descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

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

// Recursive solution:
// Call pruneTree at every subtree.
// If the current node is zero, then check if both children are None

class Solution {
public:
    TreeNode* pruneTree(TreeNode* root) {
        // Base case for an empty tree
        if (!root) {
            return nullptr;
        }

        // Case where we have a 3 node tree with 0 as its root and both
        // children are 0
        if (root->val == 0 and !root->left and !root->right) {
            delete root; // Avoid memory leaks
            return nullptr;
        }

        root->left = pruneTree(root->left);
        root->right = pruneTree(root->right);

        if (root->val == 0 and !root->left and !root->right) {
            delete root; // Avoid memory leaks
            return nullptr;
        }

        return root;
    }
};


// Iterative Solution
// Use post-order traversal and mark visited nodes with negative one
class Solution {
public:
    TreeNode* pruneTree(TreeNode* root) {
        stack<TreeNode*> stack;
        TreeNode* curr = root;
        while (curr) {
            stack.push(curr);
            curr = curr->left;
        }
        TreeNode* prev = nullptr;
        while (!stack.empty()) {
            TreeNode* curr = stack.top();
            if (!curr->right or curr->right == prev) {
                if (curr->left and curr->left->val == -1) {
                    delete curr->left;
                    curr->left = nullptr;
                }
                if (curr->right and curr->right->val == -1) {
                    delete curr->right;
                    curr->right = nullptr;
                }
                if (!curr->left and !curr->right and curr->val == 0) {
                    curr->val = -1;
                }
                stack.pop();
                prev = curr;
                continue;
            }
            prev = curr;
            curr = curr->right;
            while (curr) {
                stack.push(curr);
                curr = curr->left;
            }
        }
        return root;
    }
};