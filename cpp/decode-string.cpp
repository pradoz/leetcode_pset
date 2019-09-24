#include <vector>
#include <iostream>
#include <stack>
using namespace std;



class Solution {
public:
    string decodeString(string s) {
        string res;
        const int size = s.size();
        int i = 0;
        
        while (i < size) {
            // Start looping until we find a digit
            while (!isdigit(s[i]) and i < size) {
                res += s[i];
                ++i;
            }

            // If we obtained all the characters without finding a digit, exit
            if (i == size) {
                return res;
            }

            // We found a digit
            int num = 0;
            while (i < size and isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
                ++i;
            }

            // Handle open/closing brackets
            int j = i + 1;
            int bracket_count = 1;
            int k = 1;
            while (j < size and bracket_count > 0) {
                if (s[j] == ']') { --bracket_count; }
                if (s[j] == '[') { ++bracket_count; }
                ++j;
            }

            // Add the temp string and call it recursively on the next subseq.
            // of characters
            string temp = decodeString(s.substr(i + 1, j - i - 2));
            while (num--) {
                res += temp;
            }
            i = j;

        }
        return res;
    }
};



class Solution0 {
public:
    string decodeString(string s) {
        stack<string> string_stack;
        string curr_str;
        
        stack<int> num_stack;
        string num;

        int i = 0;

        for (char c : s) {
            if (c < 58) {
                num.push_back(c);
            }
            else if (c == '[') {
                // append the new string to the top of the stack
                string_stack.push(curr_str);

                // Add the next number
                num_stack.push(stoi(num));

                // clear the old str/num
                curr_str.clear();
                num.clear();
                
            }
            // append the closed sequence the previous-number-seen times
            else if (c == ']') {
                curr_str = string_stack.top() + helper(curr_str,
                                                             num_stack.top());
                string_stack.pop();
                num_stack.pop();
            }
            else {
                curr_str.push_back(c);                
            }
        }
        return curr_str;
    }
    
    // helper function to print characters k amount of times
    string helper(const string &s,const int k) {
        string rs = s;
        for (int i = 1; i < k; ++i) {
            rs += s;
        }
        return rs;
    }
};



int main() {
    vector<string> strings = {
        "2[a2[b]c]",     // abbcabbc
        "3[a]2[bc]",     // aaabcbc
        "3[a2[c]]",      // accaccacc
        "2[abc]3[cd]ef", // abcabccdcdcdef
    };

    for (string s : strings) {
        std::cout << Solution().decodeString(s) << std::endl;
    }
    return 0;
}