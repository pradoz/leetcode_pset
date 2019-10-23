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