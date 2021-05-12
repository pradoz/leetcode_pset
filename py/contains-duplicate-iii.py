from typing import List

# O(n) time, O(k) space
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # if the difference between two items is <= t, then:
        # -- they are in the same bucket
        # -- OR, they are in a neighboring/adjacent bucket
        buckets = {}
        adjacent = (-1, 0, 1)

        for i, num in enumerate(nums):
            bid = num // t if t != 0 else num
            for adj in adjacent:
                b = bid + adj
                # check if it is in the current or an adjacent bucket,
                # then check for condition 1
                if b in buckets and abs(buckets[b] - num) <= t:
                    return True
            buckets[bid] = num # update the current bucket

            if i >= k:
                # i - j <= k --> j > i - k
                # --> we remove the i - k^th bucket so that condition 2 holds
                expired = nums[i-k] // t if t != 0 else nums[i-k]
                buckets.pop(expired)
                # del buckets[expired]

        return False




# O(n * k) time, O(1) space -- gets TLE
class Solution0:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, i+k+1):
                if j < n:
                    x = abs(nums[i] - nums[j])
                    # y = abs(i - j)
                    if x <= t: # and y <= k:
                        return True
        return False








nums = [[1,2,3,1],[1,0,1,1],[1,5,9,1,5,9]]
k = [3, 1, 2]
t = [0, 2, 3]

test_results = [True, True, False]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.containsNearbyAlmostDuplicate(nums[i], k[i], t[i])
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
