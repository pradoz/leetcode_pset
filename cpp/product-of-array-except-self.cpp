/*
Given an array nums of n integers where n > 1,  return an array output
such that output[i] is equal to the product of all the elements of nums
except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).
*/

// O(n) time and space solution with prefixes and suffixes
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        const int n = nums.size();

        vector<int> prefixes(n, 1);
        vector<int> suffixes(n, 1);

        for (int i = 1; i < n; ++i) {
            prefixes.at(i) = prefixes.at(i-1) * nums.at(i-1);
            suffixes.at(i) = suffixes.at(i-1) * nums.at(n-i);
        }

        vector<int> ret(n);
        for (int i = 0; i < n; ++i) {
            ret.at(i) = prefixes.at(i) * suffixes.at(n-i-1);
        }
        return ret;
    }
};


// Use two integers instead of two vectors and calculate the product of the
// current index outside of the loop
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        const int n = nums.size();
        int prefix_prod = 1;
        int suffix_prod = 1;
        vector<int> ret(n, 1);
        
        for (int i = 0; i < n; ++i) {
            ret.at(i) *= prefix_prod;
            prefix_prod *= nums.at(i);
            ret.at(n-i-1) *= suffix_prod;
            suffix_prod *= nums.at(n-i-1);
        }
        return ret;
    }
};


// First attempt, used C++. Time limit exceeded due to lack of dynamic prog.
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        if (nums.size() < 2) { return 0; }
        if (nums.size() == 2) { return 1; }
        vector<int> ret(nums.size(), 1);

        for (int curr = 0; curr < nums.size(); ++curr) {
            int i = 0;
            int j = nums.size() - 1;
            while (i != curr and j != curr) {
                ret.at(curr) = ret.at(curr) * nums.at(i) * nums.at(j);
                ++i;
                --j;
            }

            while (i != j) { ret.at(curr) *= nums.at(i); ++i; }
            while (j != i) { ret.at(curr) *= nums.at(j); --j; }
        }
        return ret;
    }
};