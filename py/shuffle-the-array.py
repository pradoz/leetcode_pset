from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        i = 0
        j = n

        while i < n:
            result.append(nums[i])
            i += 1
            result.append(nums[j])
            j += 1

        return result
'''
                  n
         i        j
        [2, 5, 1, 3, 4, 7]
'''






nums = [
        [2,5,1,3,4,7],
        [1,2,3,4,4,3,2,1],
        [1,1,2,2],
       ]
n = [3, 4, 2]

test_results = [
                [2,3,5,4,1,7],
                [1,4,2,3,3,2,4,1],
                [1,2,1,2],
               ]
test_cases = len(test_results)

def run_test() -> None:
    s = Solution()
    for i in range (test_cases):
        check_test = s.shuffle(nums[i], n[i])
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
