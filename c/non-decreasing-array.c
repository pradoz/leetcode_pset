#include <cstdio>

bool checkPossibility(int* nums, int numsSize) {
    bool flag = false;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i - 1] <= nums[i]) {
            continue;
        }
        // nums[i - 1] > nums[i]
        if (flag) {
            return false;
        } 
        else {
            // no initial space, modify the front of the array
            i < 2 // you can nest ternary operators, apparently
            ? nums[i - 1] = nums[i]
            : nums[i] = (nums[i - 2] < nums[i]
                ? nums[i - 1] = nums[i]
                : nums[i - 1]);
            // if (i < 2) {
            //     nums[i - 1] = nums[i];
            // }
            // else {
            //     nums[i - 2] < nums[i]
            //     ? nums[i - 1] = nums[i]
            //     : nums[i] = nums[i - 1];
            // }
            flag = true;
        }
    }

    return true;
}



int main() {
    int arr1[4] = {-1,4,2,3};
    printf("%d\n", checkPossibility(arr1, 4)); // 1
    int arr2[4] = {3,4,2,3};
    printf("%d\n", checkPossibility(arr2, 4)); // 0
    return 0;
}