/*
Given a parentheses string, return the minimum number of parentheses we
must add to make the resulting string valid.


Example 1:
Input: "())"
Output: 1

Example 2:
Input: "((("
Output: 3
*/

// Time Complexity: O(n) since we iterate through the entire string once.
// Space Complexity: O(1) since everything is done in-place

class Solution {
public:
    int minAddToMakeValid(string S) {
        int left = 0;
        int right = 0;

        for (char c : S) {
            if (c == '(') {
                ++left;
            }
            else if (left > 0) {
                --left;
            }
            else {
                ++right;
            }
        }
        return left + right;
    }
};


// This COULD be an efficient solution if the string is guaranteed small.
// Time Complexity: O(n) since we iterate through the entire string once.
// Space Complexity: O(m) where m is the number of open parenthesis.
class Solution {
public:
    int minAddToMakeValid(string S) {
        stack<char> stk;
        int count = 0;

        for (char c : S) {
            if (c == '(') {
                stk.push(c);
            }
            else if (c == ')') {
                if (!stk.empty()) {
                    stk.pop();
                }
                else {
                    ++count;
                }
            }
        }
        return count + stk.size();
    }
};