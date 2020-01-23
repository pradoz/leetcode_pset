#include <iostream>
#include <unordered_map>
#include <queue>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;


namespace {
    void printVec(const vector<int>& v) {
        ostringstream oss;
        oss << '(';
        for (int x : v) {
            oss << x << ", ";
        }
        oss << "\b\b \b)\n";

        string result = oss.str();
        cout << result;
    }
}
// insert into heap = nlogn --> O(nlogn + k) time complexity
// we have to store all unique elements --> O(n + k) space in worst case where
//      every element is unique
// Note: if k == n, then time is n^2*logn and space is n^2.
class Solution1 {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        if (nums.empty()) {
            return {}; // returns empty vector
        }
        // get integer frequencies
        unordered_map<int, int> freq;
        for (int x : nums) {
            ++freq[x];
        }

        // pair is: <# of occurences, # which occurs>
        vector<int> result;
        priority_queue<pair<int, int>> freqVal_Key_Pairs;
        for (auto itr = freq.begin(); itr != freq.end(); ++itr) {
            freqVal_Key_Pairs.push(make_pair(itr->second, itr->first));
            if (freqVal_Key_Pairs.size() > freq.size() - k) {
                result.push_back(freqVal_Key_Pairs.top().second);
                freqVal_Key_Pairs.pop();
            }
        }

        return result;
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        if (nums.empty()) {
            return {}; // returns empty vector
        }
        // get integer frequencies
        unordered_map<int, int> freq;
        for (int x : nums) {
            ++freq[x];
        }

        // pair is: <# which occurs, # of occurences>
        vector<pair<int, int>> freqVal_Key_Pairs;
        // for (auto itr = freq.begin(); itr != freq.end(); ++itr) {
        for (auto itr : freq) {
            freqVal_Key_Pairs.push_back(make_pair(itr.first, itr.second));
        }

        // sort by greatest occurence
        sort(freqVal_Key_Pairs.begin(), freqVal_Key_Pairs.end(),
            [](const auto& lhs, const auto& rhs) {
            return lhs.second > rhs.second;
        });

        // get k largest results
        vector<int> result;
        for (int i = 0; i < k; ++i) {
            result.push_back(freqVal_Key_Pairs[i].first);
        }

        return result;
    }
};


int main() {
    Solution s;
    // Example 1:
    // Input: nums = [1,1,1,2,2,3], k = 2
    // Output: [1,2]
    int k = 2;
    vector<int> vec1 = {1,1,1,2,2,3,4,5,6};
    vector<int> result = s.topKFrequent(vec1, k);
    printVec(result);

    // Example 2:
    // Input: nums = [1], k = 1
    // Output: [1]
    k = 2;
    vector<int> vec2 = {1};
    // result.clear();
    // result = s.topKFrequent(vec2, k);
    // printVec(result);

    // Example 3:
    // Input: nums = [1,1,1,2,2,3,3,3,3], k = 2
    // Output: [1,3]
    k = 2;
    vector<int> vec3 = {1,1,1,2,2,3,3,3,3};
    // result.clear();
    // result = s.topKFrequent(vec3, k);
    // printVec(result);

    // Example 4:
    // Input: nums = [4,1,-1,2,-1,2,3], k = 2
    // Output: [-1,2]
    k = 2;
    vector<int> vec4 = {4,1,-1,2,-1,2,3};
    result.clear();
    result = s.topKFrequent(vec4, k);
    printVec(result);



    return 0;
}