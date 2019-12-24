# O(n) time for two passes
# O(n/2+1) --> O(n) since every duplicate appears twice we divide n by 2 which
# which is still linear space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = True
            else:
                seen[num] = False
                
        for num, wasSeenOnce in seen.items():
            if wasSeenOnce == True:
                return num


class Solution:
    def __init__(self):
        self.complement = 0

    def singleNumber(self, nums: List[int]) -> int:
        return self.getNumber(nums)

    def getNumber(self, arr: List[int]) -> int:
        for num in arr:
            self.complement ^= num
        return self.complement