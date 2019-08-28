class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within 
             the range [1,...,l+1] 
        """
        nums.append(0)
        i = 0
            
        n = len(nums)
        print(f'n={n}, nums={nums}')
        for i in range(len(nums)): # delete negative, elements
            if nums[i] < 0 or nums[i] >= n:
                # print(f'i={i} --> nums[i]:{nums[i]}')
                nums[i] = 0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            print(f'i={i} --> nums[i]:{nums[i]}')
            nums[nums[i] % n] += n
        for i in range(1,len(nums)):
            if nums[i] // n == 0:
                return i
        return n
''' non- working brute attempt '''
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_zero_index = -1
        nums.append(0)
        # walk through array and set negative numbers = 0
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 0

        # sort array 
        nums.sort()

        # find lowest element in range
        i = 0
        min_elem = 0
        while i < len(nums):
            print(f'i:{i} nums[i]:{nums[i]}')
            if nums[i] == 0:
                last_zero_index += 1
                print(f'last_zero_index:{last_zero_index}')
            else:
                min_elem = nums[last_zero_index + 1]
                print(f'min_elem:{min_elem}')
            i += 1

        # find max element in range
        max_elem = nums[-1]

        ## find the solution in the range
        # if lowest in element in range is > 1, return that element-1
        if min_elem == 0:
            return 1
        elif min_elem == 1:
            for i in range(len(nums)):
                if nums[i]+1 not in nums:
                    return nums[i]+1
        if min_elem != 1:
            for i in range(len(nums)):
                if min_elem-1 not in nums and nums[i]-1 > 0:
                    return min_elem-1
        else:
            return max_elem + 1 # if that element is == 1, return the max + 1

def main():
    s1 = Solution()
    ans = s1.firstMissingPositive([7,8,9,11,12])
    print(ans)

if __name__ == '__main__':
    main()
'''
def main():
    s1 = Solution()
    ans = s1.firstMissingPositive([7,8,9,11,12])
    print(ans)

if __name__ == '__main__':
    main()