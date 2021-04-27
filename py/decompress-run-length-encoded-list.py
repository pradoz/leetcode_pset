from typing import List

# O(n) / O(n*f)
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []

        n = len(nums)
        for i in range(0, n, 2):
            freq = nums[i]
            val = nums[i+1]
            result.extend([val] * freq)

        return result


# O(n) / O(n*f)
class Solution0:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        
        freqs = []
        vals = []
        n = len(nums)
        for i in range(n):
            if i % 2 == 0:
                freqs.append(nums[i])
            else:
                vals.append(nums[i])
        freq_val_pairs = list(zip(vals,freqs))

        for val, freq in freq_val_pairs:
            result += [val] * freq

        return result






nums = [[1,2,3,4], [1,1,2,3]]

test_results = [[2,4,4,4], [1,3,3]]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.decompressRLElist(nums[i])
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
