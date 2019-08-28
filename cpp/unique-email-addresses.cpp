#include <iostream>
#include <vector>
#include <unordered_set>
#include <string>
using namespace std;

class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> st;
        for(string &email : emails) {
            string cleanEmail;
            for(char c : email) {
                if(c == '+' || c == '@') break;
                if(c == '.') continue;
                cleanEmail += c;
            }
            cleanEmail += email.substr(email.find('@'));
            st.insert(cleanEmail);
        }
    return st.size();
    }
};

int main() {
    Solution s1;

    vector<string> vec = {"testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"};
    cout << s1.numUniqueEmails(vec) << endl;

    return 0;
}