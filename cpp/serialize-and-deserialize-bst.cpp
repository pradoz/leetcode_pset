/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string order;
        preorderDFS(root, order);
        return order;
    }
    
    inline void preorderDFS(TreeNode* root, string& order) {
        if (!root) return ;
        char buff[4];
        memcpy(buff, &(root->val), sizeof(int));
        for (int i = 0; i < 4; ++i) {
            order.push_back(buff[i]);
        }
        preorderDFS(root->left, order);
        preorderDFS(root->right, order);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int pos = 0;
        return reconstruct(data, pos, INT_MIN, INT_MAX);
    }
    
    inline TreeNode* reconstruct(const string& buffer, int& pos, int minValue, int maxValue) {
        if (pos >= buffer.size()) return NULL; //using pos to check whether buffer ends is better than using char* directly.
        
        int value;
        memcpy(&value, &buffer[pos], sizeof(int));
        if (value < minValue or value > maxValue) return NULL;
        
        TreeNode* node = new TreeNode(value);
        pos += sizeof(int);
        node->left = reconstruct(buffer, pos, minValue, value);
        node->right = reconstruct(buffer, pos, value, maxValue);
        return node;
    }
};


// couldn't quit pull off the python solution in cpp :(
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) {
            return "0";
        }

        encrypt += 1;
        decrypt = (to_string(root->val));
        // struct_list.push_back("1");
        // data_list.push_back(to_string(root->val));
        serialize(root->left);
        serialize(root->right);
        return encrypt;
    }
    

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data.size() < 1) {
            return nullptr;
        }

        // string b = static_cast<string>(struct_list.front());
        // struct_list.pop_front();
        int count = 0;
        string b = encrypt[0];
        encrypt.erase(0);

        if (b == "1") {
            // string val = static_cast<string>(data_list.front());
            string val = decrypt[0];
            decrypt.erase(0);

            TreeNode* root = new TreeNode(stoi(val));
            // data_list.pop_front();
            root->left = deserialize(data);
            root->right = deserialize(data);
            return root;
        }
        return nullptr;
    }
private:
    string encrypt;
    string decrypt;
};


// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));