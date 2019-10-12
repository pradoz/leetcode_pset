// #include <cstring>
// #include <string>
// using namespace std;

class Node {
public:
    Node() {
        is_word = false;
        memset(next, 0, sizeof(next));
    }

    Node* next[26];
    bool is_word;
};

class Trie {
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new Node();
    }
    
    ~Trie() {
        clear(root);
    }

    /** Inserts a word into the trie. */
    void insert(const string& word) {
        auto temp = root;
        for (int i = 0; i < word.size(); ++i) {
            if (!(temp->next[word[i] - 'a'])) {
                temp->next[word[i] - 'a'] = new Node();
            }
            temp = temp->next[word[i]-'a'];
        }
        temp->is_word = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(const string& word) {
        auto temp = find_string(word);
        if (temp and temp->is_word) {
            return true;
        }
        else {
            return false;
        }
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(const string& prefix) {
        auto temp = find_string(prefix);
        if (temp) {
            return true;
        }
        else {
            return false;
        }
    }

private:
    Node* root;


    Node* find_string(const string& word) {
        auto temp = root;
        for (int i = 0; i < word.size(); ++i) {
            if (temp->next[word[i] - 'a']) {
                temp = temp -> next[word[i] - 'a'];
            }
            else {
                temp = nullptr;
                break;
            }
        }
        return temp;
    }

    // clear() cleans up trie nodes so we don't leak memory
    void clear(Node* root) {
        for (int i = 0; i < 26; ++i) {
            if (root->next[i]) {
                clear(root->next[i]);
            }
        }
        delete root;
    }
};


// Your Trie object will be instantiated and called as such:
// Trie obj = new Trie();
// obj.insert(word);
// bool param_2 = obj.search(word);
// bool param_3 = obj.startsWith(prefix);