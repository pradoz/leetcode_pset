#include <iostream>
#include <vector>

using namespace std;

// Challenge: Use O(1) extra space
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        const int size = nums.size();
        int new_length = 0;

        for (int i = 0; i < size; ++i) {
            if (i == 0 or nums[i] != nums[i-1]) {
                nums[new_length] = nums[i];
                new_length++;
            }
        }
        return new_length;
    }
};



int main() {
    vector<int> vec = {0,0,1,1,1,2,2,3,3,4};
    Solution s;
    int new_len = s.removeDuplicates(vec);
    cout << "length after duplicates removed: " << new_len << endl;

    // for (int num = 0; num < vec.size(); ++num) {
    //     cout << vec[num] << ", ";
    // }
    // cout << endl;

    return 0;
}