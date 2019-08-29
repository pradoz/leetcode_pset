/*
Given an integer array with no duplicates. A maximum tree building on this
array is defined as follow:

  1. The root is the maximum number in the array.
  2. The left subtree is the maximum tree constructed from left part subarray 
    divided by the maximum number.
  3. The right subtree is the maximum tree constructed from right part subarray 
    divided by the maximum number.

Construct the maximum tree by the given array and output the root node of
this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
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


// Recursive with a helper function
class Solution {
public:
   TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return help_construct(nums, 0, nums.size() - 1);
    }
    
    TreeNode* help_construct(vector<int>& nums, int left, int right) {
        if (left > right) {
            return nullptr;
        }
        
        int max_idx = left;
        for (int i = left; i <= right; ++i){
            if (nums[i] > nums[max_idx]) {
                max_idx = i; 
            }
        }
        
        TreeNode* root = new TreeNode(nums[max_idx]);
        root->left = help_construct(nums, left, max_idx - 1);
        root->right = help_construct(nums, max_idx + 1, right);
        return root;
    }
};


// Using a stack iteratively
class Solution {
public:
   TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        stack<TreeNode*> stk;
        for (int num : nums) {
            TreeNode* curr = new TreeNode(num);

            while (!stk.empty() and stk.top()->val < curr->val) {
                curr->left = stk.top();
                stk.pop();
            }

            if (!stk.empty()) {
                stk.top()->right = curr;
            }
            stk.push(curr);
        }

        // pop the stack until one node remains
        while (stk.size() > 1) {
            stk.pop();
        }
        return stk.top();
    }
};


// Using a vector iteratively
class Solution {
public:
   TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        vector<TreeNode*> vec;
        for (int i = 0; i < nums.size(); ++i) {
            TreeNode* curr = new TreeNode(nums.at(i));

            while (!vec.empty() and vec.back()->val < nums.at(i)) {
                curr->left = vec.back();
                vec.pop_back();
            }

            if (!vec.empty()) {
                vec.back()->right = curr;
            }
            vec.push_back(curr);
        }
        return vec.front();
    }
};


// using a map
// 1. Populate right subtree if numbers are decreasing.
// 2. If the current number is larger, the portion of the right subtree that is
//    smaller becomes a left subtree of the current number
// 3. Now, the current number is the leaf/smallest in the right subtree.
class Solution {
public:
   TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        map<int, TreeNode*> node_map;

        for (int num : nums) {
            auto itr = node_map.insert({num, new TreeNode(num)}).first;

            if (itr != node_map.begin()) {
                itr->second->left = next(itr, -1)-> second;
                node_map.erase(node_map.begin(), itr);
            }
            if (next(itr, 1) != node_map.end()) {
                next(itr, 1)->second->right = itr->second;
            }
        }
        return node_map.rbegin()->second;
    }
};