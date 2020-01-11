/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int* result = malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;

    int p = 1;

    for(int i = 0; i < numsSize; ++i) {
        result[i] = p;
        p *= nums[i];
    }

    p = 1;
    for(int i = numsSize - 1; i >= 0; --i) {
        result[i] *= p;
        p *= nums[i];
    }
    return result;
}