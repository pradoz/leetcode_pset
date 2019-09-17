/*
  1. Record the length of the current continuous increasing subsequence
     which ends with "nums[i]" as "length_of_current_sub"
  2. Use "length_of_max_sub" to record the maximum value of "curr"
*/
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int length_of_max_sub = 0;
        int length_of_current_sub = 0;

        for (int i = 0; i < nums.size(); ++i) {
            // This short-circuit-evaluates when i=0 since nums[i-1] would
            // normally be out of bounds.
            if (i == 0 or nums[i-1] < nums[i]) {
                // We are still increasing
                ++length_of_current_sub;
                length_of_max_sub = max(length_of_max_sub, length_of_current_sub);
            }
            else {
                length_of_current_sub = 1;
            }
        }
        return length_of_max_sub;
    }
};


// Dynamic programming approach
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
            
        vector<int> dp_vec(nums.size(), 1);
        int ret = 1;
        for (int i = 1; i < nums.size(); ++i) {
            dp_vec[i] = dp_vec[i - 1];
            if (nums[i] > nums[i - 1]) {
                // Still increasing, increase the index
                ++dp_vec[i];
            }
            else {
                // Reset if the condition was broken
                dp_vec[i] = 1;
            }
            ret = max(ret, dp_vec[i]);
        }
            
        return ret;
    }
};


// Two pointer solution
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int max_sub_length = 0;
        for (int i = 0, curr = 0; curr < nums.size(); ++curr) {
            // Record and reset the current length
            if (curr == 0 or nums[curr] <= nums[curr - 1]) {
                i = curr;
            }
            max_sub_length = max(max_sub_length, curr - (i - 1));
        }
        return max_sub_length;
    }
};