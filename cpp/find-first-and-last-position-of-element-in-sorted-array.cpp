// recursive
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        const int size = nums.size() - 1;
        int first = binarySearch(nums, 0, size, target, true);
        int last = binarySearch(nums, 0, size, target, false);
        return {first, last};
    }

private:
    int binarySearch(const vector<int>& nums, int low, int high, int target, bool findFirst) {
        if (high < low) {
            return -1;
        }

        int mid = (high + low) / 2;

        if (findFirst == true) {
            if ((mid == 0 or target > nums[mid - 1]) and nums[mid] == target) {
                return mid;
            }
            else if (target > nums[mid]) {
                return binarySearch(nums, mid + 1, high, findFirst);
            }
            else {
                return binarySearch(nums, low, mid - 1, findFirst);
            }
        }
        else {
            if ((mid == nums.size() - 1 or target < nums[mid + 1]) and nums[mid] == target) {
                return mid;
            }
            else if (target < nums[mid]) {
                return binarySearch(nums, low, mid - 1, findFirst);
            }
            else {
                return binarySearch(nums, mid + 1, high, findFirst);
            }
        }
    }
};


// iterative
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        const int size = nums.size() - 1;
        int first = binarySearch(nums, 0, size, target, true);
        int last = binarySearch(nums, 0, size, target, false);
        return {first, last};
    }

private:
    int binarySearch(const vector<int>& nums, int low, int high, int target, bool findFirst) {
        while (1) {
            if (high < low) {
                return -1;
            }

            int mid = (high + low) / 2;

            if (findFirst == true) {
                if ((mid == 0 or target > nums[mid - 1]) and nums[mid] == target) {
                    return mid;
                }
                else if (target > nums[mid]) {
                    low = mid + 1;
                }
                else {
                    high = mid - 1;
                }
            }
            else {
                if ((mid == nums.size() - 1 or target < nums[mid + 1]) and nums[mid] == target) {
                    return mid;
                }
                else if (target < nums[mid]) {
                    high = mid - 1;
                }
                else {
                    low = mid + 1;
                }
            }
        }
    }
};


