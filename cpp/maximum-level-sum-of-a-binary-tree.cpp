/*
Given the root of a binary tree, the level of its root is 1,
the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values
of nodes at level X is maximal.
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


// DFS
class Solution {
public:
    int maxLevelSum(TreeNode* root, int max_level = 0) {
        dfs(root, 1);
        for (int i = 0; i < sums.size(); ++i) {
            if (sums[i] > sums[max_level]) {
                max_level = i;
            }
        }
        return max_level + 1;
    }

private:
    vector<int> sums;

    void dfs(TreeNode* root, int level) {
        if (!root) {
            return ;
        }
        if (sums.size() < level) {
            sums.resize(level);
        }
        sums[level - 1] += root->val;

        dfs(root->left, level + 1);
        dfs(root->right, level + 1);
    }
};


// BFS with a queue
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        if (!root) {
            return 0;
        }

        q.push(root);
        int level = 1;
        while (!q.empty()) {
            int sz = q.size();
            int curr_sum = 0;
            for (int i = 0; i < sz; ++i) {
                curr_sum += q.front()->val;
                if (q.front()->left) {
                    q.push(q.front()->left);
                }
                if (q.front()->right) {
                    q.push(q.front()->right);
                }
                q.pop();
            }
            if (max_sum < curr_sum) {
                max_sum = curr_sum;
                max_level = level;
            }
            ++level;
        }
        return max_level;
    }

private:
    queue<TreeNode*> q;
    int res = 0, max_level = 1, max_sum = INT_MIN;
};



// Using two vectors: one for all level sums and, one for the nodes on the
// current level
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        if (!root) {
            return 0;
        }


        TreeNode* curr = root;

        while (1) {
            if (curr->left) {
                stack.push_back(curr);
                TreeNode* next = curr->left;
                curr->left = nullptr;
                curr = next;
            }
            else if (curr->right) {
                stack.push_back(curr);
                TreeNode* next = curr->right;
                curr->right = nullptr;
                curr = next;
            }
            else {
                int level = stack.size();
                if (sum.size() <= level) {
                    sum.resize(level + 1);
                }
                sum[level] += curr->val;

                // Break condition
                if (stack.empty()) {
                    break;
                }

                curr = stack.back();
                stack.pop_back();
            }
        }

        int max_level = sum.size();
        int max_val = INT_MIN;
        for (int i = 1; i < sum.size(); ++i) {
            if (max_val < sum[i]) {
                max_val = sum[i];
                max_level = i;
            }
        }
        return max_level + 1;
    }

private:
    vector<int> sum;
    vector<TreeNode*> stack;
};