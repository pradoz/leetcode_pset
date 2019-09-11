/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

/*
Solution Explanation:
1. Keep a counter and constuct nodes until we reach the size of the list.
2. Create a new, root and increment the counter.
3. Recursively call bstFromPreorder() on the current node's left subtree and
    right subtree.
*/

// Using Bounds Algorithm:
// Time complexity: O(n) since we call bstFromPreorder exactly n times.
// Space complexity: O(n), in the worst case we have to store all of the nodes
//   as we construct the tree
class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder, int upper_bound = INT_MAX) {
        if (i == preorder.size() or preorder.at(i) > upper_bound) {
            return nullptr;
        }

        TreeNode* root = new TreeNode(preorder[i]);
        ++i;
        root->left = bstFromPreorder(preorder, root->val);
        root->right = bstFromPreorder(preorder, upper_bound);
        return root;
    }
private:
    int i = 0;
};


// Using an Iterative Stack Algorithm:
// Time complexity: O(n) since we linearly visit every node and perform checks.
// Space complexity: O(n), in the worst case we have to store all of the nodes
//   as we construct the tree
class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder, int upper_bound = INT_MAX) {
        TreeNode* root = new TreeNode(preorder[0]);
        stack<TreeNode*> node_stack;
        node_stack.push(root);

        for (int i = 1; i < preorder.size(); ++i) {
            TreeNode* curr = new TreeNode(preorder[i]);
            if (curr->val < node_stack.top()->val) {
                node_stack.top()->left = curr;
            }
            else {
                TreeNode* prev = nullptr;
                while (!node_stack.empty() and node_stack.top()->val < curr->val) {
                    prev = node_stack.top();
                    node_stack.pop();
                }
                prev->right = curr;
            }
            node_stack.push(curr);
        }
        return root;
    }
};

/*
Solution Explanation:
1. If the list is empty, we cannot construct a tree.
2. Split the list where the values stop decreasing/start increasing.
3. Recursively call bstFromPreorder() on the left and right subtrees.
*/

// Time Complexity: O(n^2) worst case, O(n log n) on average.
// Space Complexity: O(n) worst case, O(logn) one average.
class Solution {
public:
    TreeNode* bstFromPreorder(vector<int> &preorder, int first = 0, int last = 0) {
        if (last == 0) {
            last = preorder.size();
        }
        if (first == last) {
            return nullptr;
        }

        auto split = find_if(begin(preorder) + first,
                             begin(preorder) + last,
                             [&](int val) {
                                return val > preorder[first];
                             });
        auto root = new TreeNode(preorder[first]);
        root->left = bstFromPreorder(preorder,
                                     first + 1, split - begin(preorder));
        root->right = bstFromPreorder(preorder,
                                     split - begin(preorder), last);
        return root;
    }
};