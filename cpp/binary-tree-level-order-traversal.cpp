/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// Iterative goodness
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ret;
        TreeNode* temp = nullptr;

        int curr_level = 0;
        if (!root) {
            return ret;
        }

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            curr_level = q.size();
            vector<int> levels;

            while (curr_level--) {
                temp = q.front();
                levels.push_back(temp->val);
                if (temp->left != nullptr) {
                    q.push(temp->left);
                }
                if (temp->right != nullptr) {
                    q.push(temp->right);
                }
                q.pop();
            }
            ret.push_back(levels);
        }
        return ret;
    }
};


// Recursive preorder traversal to build a vector
class Solution {
public:
    void build_vector(TreeNode* root, int height) {
        if (!root) {
            return ;
        }
        if (ret.size() == height) {
            ret.push_back(vector<int>());
        }

        ret.at(height).push_back(root->val);

        build_vector(root->left, height + 1);
        build_vector(root->right, height + 1);

    }

    vector<vector<int>> levelOrder(TreeNode* root) {
        build_vector(root, 0);
        return ret;
    }
private:
    vector<vector<int>> ret;
};