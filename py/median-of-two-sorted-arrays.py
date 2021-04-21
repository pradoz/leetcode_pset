from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = 0.0

        if not nums1:
            return float(nums2[0] + nums2[len(nums2)-1]) / 2.0
        if not nums2:
            return float(nums1[0] + nums1[len(nums1)-1]) / 2.0

        left1 = left2 = 0
        right1 = len(nums1) - 1
        right2 = len(nums2) - 1

        while left1 <= right1 and left2 <= right2:
            print(f'{nums1[left1]}, {nums1[right1]}, {nums2[left2]}, {nums2[right2]}')
            if nums1[left1] == nums1[right1] == nums2[left2] == nums2[right2]:
                result = nums1[left1]
                break
            if nums1[left1] < nums2[left2]:
                left1 += 1
            else:
                left2 += 1

            if nums1[right1] < nums2[right2]:
                right1 -= 1
            else:
                right2 -= 1






        return result








nums1 = [[1,3],[1,2],[0,0],[],[2]]
nums2 = [[2],[3,4],[0,0],[1],[]]

test_results = [2.0, 2.5, 0.0, 1.0, 2.0]
test_cases = len(test_results)

def run_test() -> None:
    s = Solution()
    for i in range (test_cases):
        check_test = s.findMedianSortedArrays(nums1[i], nums2[i])
        test_flag = True if check_test == test_results[i] else False
        if test_flag == True:
            print(f'++++ TEST #{i+1}: SUCCESS. Result = {check_test}')
        else:
            print(f'---- TEST #{i+1}: FAILURE.')
            print(f'       Expected: {test_results[i]}')
            print(f'       Received: {check_test}')

def main() -> None:
    run_test()

if __name__ == '__main__':
    main()
