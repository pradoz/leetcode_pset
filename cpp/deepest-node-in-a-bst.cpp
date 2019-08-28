/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */
class Solution {
public:
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        while (root) {
            int lhs = get_depth(root->left);
            int rhs = get_depth(root->right);

            if (lhs == rhs) { return root; }
            else if (lhs > rhs) { root = root->left; }
            else { root = root->right; }
        }
    }

private:
    int get_depth(TreeNode* root) {
        if (!root) { return 0; }
        int lhs = get_depth(root->left);
        int rhs = get_depth(root->right);
        return lhs > rhs ? lhs + 1 : rhs + 1;
    }
};


class Solution {
public:
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        int left_val = -1, right_val = -1;
        max_depth(root->left, 0, left_val);
        max_depth(root->right, 0, right_val);
        if (left_val > right_val) {
            return subtreeWithAllDeepest(root->left);
        }
        else if (left_val < right_val) {
            return subtreeWithAllDeepest(root->right);
        }
        else {
            return root;
        }
    }
    
private:
    void max_depth(TreeNode* root, int level, int& val){
        if (!root) return ;
        val = max(val, level);
        max_depth(root->left, level + 1, val);
        max_depth(root->right, level + 1, val);
    }
};


// Using a queue
class Solution {
public:
    std::vector<TreeNode*> findNodesDeepestLevel(TreeNode* root) {
        if (!root) { return {}; }

        std::queue<TreeNode*> q;
        q.push(root);
        std::vector<std::vector<TreeNode*>> levels;


        // Push all of the nodes on to a queue of vectors, where each vector,
        // or index in the queue, is a different level in the tree
        while (!q.empty()) {
            int size = q.size();
            std::vector<TreeNode*> arr {};
            while (size > 0) {
                TreeNode* tmp = q.front();
                q.pop();
                arr.push_back(tmp);
                if (tmp->left) { q.push(tmp->left); }
                if (tmp->right) { q.push(tmp->right); }
                --size;
            }
            levels.push_back(arr); // empty the queue into a new level
        }
        return levels.back();
    }
    
    TreeNode* findParent(TreeNode* root, int label) {
        if (!root) {
            return nullptr;
        }
        if (root->left) {
            if (root->left->val == label) {
                return root;
            }
        }
        if (root->right) {
            if (root->right->val == label) {
                return root;
            }
        }
        TreeNode* a = findParent(root->left, label);
        if (a) {
            return a;
        }
        return findParent(root->right, label);
    }
    
    int computeLevel(TreeNode* root, int node, int level) {
        if (!root) {
            return 0;
        }
        if (root->val == node) {
            return level;
        }
        int downLevel = computeLevel(root->left, node, level+1);
        if (downLevel != 0) {
            return downLevel;
        }
        return computeLevel(root->right, node, level+1);
    }
    
    TreeNode* findNode(TreeNode* root, int label) {
        if (!root) {
            return nullptr;
        }
        if (root->val == label) {
            return root;
        }
        TreeNode* a = findNode(root->left, label);
        if (a) {
            return a;
        }
        return findNode(root->right, label);
    }
    
    bool findPath(TreeNode* root, TreeNode* p, std::vector<TreeNode*>& path) {
        if (!root) return false;

        path.emplace_back(root);
        
        if (root->val == p->val) return true;
        
        if (findPath(root->left, p, path) or findPath(root->right, p, path))
            return true;
        
        path.pop_back();
        return false;
    }
    
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        std::vector<TreeNode*> path_p;
        findPath(root, p, path_p);

        std::vector<TreeNode*> path_q;
        findPath(root, q, path_q);

        std::unordered_set<TreeNode*> unord_set;
        for (int i = 0; i < path_q.size(); i++) {
            unord_set.emplace(path_q[i]);
        }
        for (int i = path_p.size()-1; i>= 0; i--) {
            auto it = unord_set.find(path_p[i]);
            if (it != unord_set.end()) {
                return *it;
            }
        }
        return nullptr;
    }
    
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        if (!root) { return nullptr; }
        if (!root->left && !root->right) { return root; }

        std::vector<TreeNode*> nodes = findNodesDeepestLevel(root);
        if (nodes.size() == 1) {
            return findNode(root, nodes.front()->val);
        }

        TreeNode* tmp {nullptr};
        int min_level = INT_MAX;
        for (int i = 0; i < nodes.size(); ++i) {
            for (int j = i+1; j < nodes.size(); ++j) {
                TreeNode* a = lowestCommonAncestor(root, nodes[i], nodes[j]);
                int level = computeLevel(root, a->val,1);
                if (level < min_level) {
                    tmp = a;
                    min_level = level;
                }
            }
        }
        return tmp; 
    }
};









