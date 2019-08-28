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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (nums.empty()) return nullptr;

        const unsigned int size = nums.size() / 2;
        TreeNode* root = new TreeNode(nums[size]);

        vector<int> left(nums.begin(), nums.begin() + nums.size() / 2);
        vector<int> right(nums.begin() + nums.size() / 2 + 1, nums.end());

        root->left = sortedArrayToBST(left);
        root->right = sortedArrayToBST(right);

        return root;
    }
};

class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (nums.size() == 0) { return nullptr; }

        queue<TreeNode*> node_queue;
        int count = 0;

        TreeNode* root = new TreeNode(0);
        TreeNode* current = nullptr;

        node_queue.push(root);
        ++count;

        while (count < nums.size()) {
            current = node_queue.front();
            node_queue.pop();
            current->left = new TreeNode(0);
            ++count;
            node_queue.push(current->left);
            
            if (count < nums.size()) {
                current->right = new TreeNode(0);
                ++count;
                node_queue.push(current->right);
            }
        }
        int i = 0;
        populate(root, nums, i);
        return root;
        
    }
    
    void populate(TreeNode* root, vector<int>& nums, int &i){
        if (!root) { return; }
        populate(root->left, nums, i);
        root->val=nums[i];
        ++i;
        populate(root->right, nums, i);
    }
    
    
};