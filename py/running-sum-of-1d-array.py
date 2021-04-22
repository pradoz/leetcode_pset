from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums


class Solution0:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = nums[0]
        # p=p+num --> nums[i]
        # use a temp variable to avoid allocating a new array
        # if we needed a thread-safe implementation, we shouldn't modify this
        # array in-place and allocate an auxilarry array instead
        for i in range(1, len(nums)):
            temp = nums[i]
            nums[i] += prefix
            prefix += temp
        return nums








nums = [[1,2,3,4],[1,1,1,1,1],[3,1,2,10,1]]

test_results = [[1,3,6,10],[1,2,3,4,5],[3,4,6,16,17]]
test_cases = len(test_results)

def run_test() -> None:
    s = Solution()
    for i in range (test_cases):
        check_test = s.runningSum(nums[i])
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
