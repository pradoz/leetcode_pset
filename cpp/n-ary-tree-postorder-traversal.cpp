/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
// Recursively without DFS
class Solution {
public:
    vector<int> postorder(Node* root) {
        if (!root) return {};
        vector<int> res;
        vector<Node*> nodes = {root};
        while (!nodes.empty()) {
            Node* back = nodes.back();
            nodes.pop_back();
            res.push_back(back->val);
            nodes.insert(nodes.end(),
                         back->children.begin(),
                         back->children.end());
        }
        reverse(res.begin(), res.end());
        return res;
    }
};


// Recursively using DFS
class Solution {
public:
    void dfs(Node* root, vector<int>& ret) {
        if (!root) { return ; }

        for (auto& child : root->children) {
            dfs(child, ret);
        }
        ret.push_back(root->val);
    }
    vector<int> postorder(Node* root) {
        vector<int> ret;
        dfs(root, ret);
        return ret;
    }
};


// Iteratively
class Solution {
public:
    vector<int> postorder(Node* root) {
        stack<Node*> st;
        st.push(root);
        vector<int> result;
        while (!st.empty() and root) {
            Node* n = st.top();
            st.pop();
            result.insert(result.begin(), n->val);
            for (auto& child : n->children) {
                st.push(child);
            }
        }
        return result;
    }
};

