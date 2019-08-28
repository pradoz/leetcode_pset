/*
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

// O(n^2) runtime solution, O(1) extra space
// using bounds checking, const where necessary etc.
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        const int size = nums.size();

        if (size == 2) {
            return {0, 1};
        }

        for (int i = 0; i < size; ++i) {
            for (int j = 0; j < size; ++j) {
                if (nums.at(i) + nums.at(j) == target and i != j) {
                    return {i, j};
                }
            }
        }
        return {0, 0};
    }
};


// O(n^2) runtime solution, O(1) extra space
// minimal space, removed bounds checking, removed trivial case check
// reduced search space of j so we no longer have to check i != j
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); ++i) {
            for (int j = i + 1; j < nums.size(); ++j) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {0, 0};
    }
};



// O(n) runtime+space solution, is the # of unique integers in nums
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        vector<int> ret;
        int size = nums.size();
    
        for (int i = 0; i < size; ++i) {
            if (map.find(target - nums[i]) != map.end()) {
                ret.push_back(map[target - nums[i]]);
                ret.push_back(i);
                break;
            }
            map[nums[i]] = i;
        }
        return ret;
    }
};