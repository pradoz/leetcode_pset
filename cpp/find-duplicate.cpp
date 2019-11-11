// count frequencies with map
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_map<int, int> map;

        for (int x : nums) {
            if (map.find(x) != map.end()) {
                return x;
            }
            map[x] = 1;
        }
        assert(false);
    }
};

// floyd's algorithm for cycle detection
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int fast = 0;
        int slow = 0;

        do {
            fast = nums[nums[fast]];
            std::cout << "XXXX = nums[nums[fast]]" << nums[nums[fast]] << std::endl;
            slow = nums[slow];
            std::cout << "XXXX = nums[slow]" << nums[slow] << std::endl;
        } while (fast != slow);

        fast = 0;
        while (fast != slow) {
            fast = nums[fast];
            slow = nums[slow];
        }
        return slow;
    }
};