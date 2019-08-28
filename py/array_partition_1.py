'''
Input: [1,4,3,2]
Output: 4
Explanation: n is 2, and the maximum sum of pairs is
4 = min(1, 2) + min(3, 4).
'''

# Time:  O(nlogn)
# Space: O(1)
# Notes: We could use O(n) space with sort(nums) if we need to return a new list

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 0

        nums.sort()
        return sum(nums[::2])
        
        # Alternate Solution
        # for i in range(0, len(nums), 2): # step size 2
        #     max_sum += nums[i]
        # return max_sum




def main():
    s1 = Solution()
    ans = s1.subarraySum([1,4,3,2,5,1,6,8,2])
    print(ans)

if __name__ == '__main__':
    main()