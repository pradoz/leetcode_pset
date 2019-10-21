#include <iostream>
#include <vector>

using namespace std;

// Challenge: Use O(1) extra space
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        const int size = nums.size();
        int duplicate_count = 0;

        for (int i = 0; i < size; ++i) {
            if (i == 0 or nums[i] != nums[i-1]) {
                nums[duplicate_count] = nums[i];
                duplicate_count++;
            }
        }
        return duplicate_count;
    }
};



int main() {
    vector<int> vec = {1,1,2,3,4,5,6,6,6,7,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,10,10};
    Solution s;
    int dupes = s.removeDuplicates(vec);
    cout << "Duplicates removed: " << dupes << endl;

    // for (int num = 0; num < vec.size(); ++num) {
    //     cout << vec[num] << ", ";
    // }
    // cout << endl;

    return 0;
}