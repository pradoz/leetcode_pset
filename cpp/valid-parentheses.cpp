#include <iostream>
#include <string>
using namespace std;


class Solution {
public:
    bool isValid(string s) {
        string stack;
        for (char bracket : s) {
            // append opening brackets to the stack string
            if (bracket == '(' or bracket == '[' or bracket == '{') {
                stack += bracket;
            }
            else {
                // return false if the stack is empty and the brack is a
                // closing bracket 
                // Note: each bracket character differs by 2 in the ASCII table
                if (stack.empty() or abs(stack.back() - bracket) > 2) {
                    // cout << "XXXX abs(" << stack.back() << " - " << bracket << ")= " << abs(stack.back() - bracket) << endl;
                    return false;
                }
                // pop back of the string "Stack" to keep a FIFO order
                stack.pop_back();
            }
        }

        // if the stack contains any brackets, then we have an invalid sequence
        return stack.empty();
    }
};

int main() {
    Solution s;
    cout << s.isValid("()") << endl;
    cout << s.isValid("(()") << endl;
    cout << s.isValid("{()}") << endl;
    cout << s.isValid("{()}}}}]]") << endl;
    return 0;
}