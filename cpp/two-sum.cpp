// quadratic runtime, inplace solution (brute force method)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        const int size = nums.size();
        if (size == 2) {
            return {0, 1};
        }

        for (int i = 0; i < size; ++i) {
            for (int j = i + 1; j < size; ++j) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        assert(false);
    }
};


// O(n) solution using a map and the distance from each sum
// the map stores each array value as a key, and its index as a value.
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> distances;
        for (int i = 0; i < nums.size(); ++i) {
            int check = target - nums[i];
            if (distances.find(check) != distances.end()) {
                return {i, distances[check]};
            }
            distances[nums[i]] = i;
        }
        assert(false);
    }
};



class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> ret;
        for (int i = 0; i < nums.size(); ++i) {
            int a = nums[i];
            int b = target - nums[i];
            if (ret.count(b)) {
                return vector<int>{i, ret[b]};
            }
            ret[nums[i]] = i;
        }
        assert(false); // avoid error for not reaching end return statement
    }
};