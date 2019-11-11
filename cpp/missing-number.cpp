#include <iostream>
#include <vector>
using namespace std;



// Note:
// Your algorithm should run in linear runtime complexity.
// Could you implement it using only constant extra space complexity?

// 2n passes --> big Oh of n: O(n), done in-place --> O(1) space.
class Solution0 {
public:
    int missingNumber(vector<int>& nums) {
        const int size = nums.size();
        int missing_num = 0;

        for (int i = 0; i <= size; ++i) {
            missing_num ^= i;
        }

        for (int n : nums) {
            missing_num ^= n;
        }

        return missing_num;
    }
};
/*
Every "----" indicates the XOR (binary addition) operation applied on the above
sets of 4 bits.

i=0
0000 --> 0

i=1
0000
0001
----
0001 --> 1

i=2
0010
0001
----
0011 --> 3

i=3
0011
0011
----
0000 --> 0

i=4
0100
0000
----
0100 --> 4

i=5
0100
0101
----
0001 --> 1
----------------------
[1,2,3,5] --> missing 4 example:

x=1
0001
0001
----
0000 --> 0

x=2
0000
0010
----
0010 --> 2

x=3
0010
0011
----
0001 --> 1

x=5
0001
1001
----
1000 --> 4

Answer: 4
*/

class Solution1 {
public:
    int missingNumber(vector<int>& nums) {
        const int size = nums.size();
        for (int i = 0; i < size; ++i) {
            while (nums[i] != size and nums[i] != i) {
                swap(nums[i], nums[nums[i]]);
            }
        }
        for (int i = 0; i < size; ++i) {
            if (nums[i] != i) {
                return i;
            }
        }
        return size;
    }
};

// We know that sum(1,2,3,...,n) = n(n+1)/2
class Solution3 {
public:
    int missingNumber(vector<int>& nums) {
        const int n = nums.size();
        int sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            sum += nums[i];
        }
        sum = (n*(n+1)/2) - sum;

        return sum;
    }
};

#include <numeric>
// funny one-liner
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        return ((nums.size()*(nums.size()+1)/2) - accumulate(nums.begin(), nums.end(), 0));
    }
};




int main() {
    vector<int> nums = {9,6,4,2,3,5,7,0,1,10,11,12,13,8,14,15,16};
    Solution s;
    s.missingNumber(nums);
    return 0;
}