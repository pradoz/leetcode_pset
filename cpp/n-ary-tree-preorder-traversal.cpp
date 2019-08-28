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

// Recusive (DFS-ish)
class Solution {
private:
    void traverse_tree(Node* root, vector<int>& res) {
        if (!root)
            return ;

        res.push_back(root->val);

        for (auto child : root->children)
            traverse_tree(child, res);
    }

public:
    vector<int> preorder(Node* root) {
        vector<int> res;

        traverse_tree(root, res);

        return res;
    }
};

// Iteratively, with a stack
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> ret;
        if (!root) return ret;

        stack<Node*> s;
        s.push(root);
        while (!s.empty()) {
            Node* curr = s.top();
            s.pop();
            ret.push_back(curr->val);

            for (int i = curr->children.size()-1; i >=0; --i)
                if (curr->children[i])
                    s.push(curr->children[i]);
        }
        return ret;
    }
};


// Helper functions
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> values;
        recurse(root, values);
        iterate(root, values);
        return values;
    }

    void recurse(Node* node, vector<int>& values) {
        if (!node) return ;

        values.push_back(node->val);
        for (auto node : node->children) {
            recurse(node, values);
        }
    }

    void iterate(Node* root, vector<int>& values) {
        if (!root) return ;
    }
};

// Withe a deque, iteratively
class Solution {
public:
    vector<int> preorder(Node* root) {
        if (!root) return {};
        vector<int> values;
        iterate(root, values);
        return values;
    }

    void iterate(Node* root, vector<int>& values) {
        if (!root) return ;

        deque<Node*> nodes;
        nodes.push_front(root);

        while (!nodes.empty()) {
            const auto node = nodes.front();
            nodes.pop_front();
            values.push_back(node->val);

            // Traverse with reverse iterators
            for (auto itr = node->children.rbegin(); itr != node->children.rend(); ++itr) {
                nodes.push_front(*itr);
            }
        }
    }
};



class Solution {
public:
  vector<int> preorder(Node* root) {
    vector<int> values;
    if (root) preorder(root, values);
    return values;
  }
    
  void preorder(Node* node, vector<int>& values) {
    values.push_back(node->val);
    for (const auto& node : node->children) {
      preorder(node, values);
    }
  }
};






