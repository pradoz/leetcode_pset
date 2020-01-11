class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1

        temp = []
        for key, val in frequencies.items():
            temp.append((key, val))

        temp.sort(key=lambda x: x[1], reverse=True)
        result = []
        counter = 0
        while counter < k:
            result.append(temp[counter][0])
            counter += 1

        return result


print(Solution().topKFrequent([1,1,1,2,2,3,3,3,3], 2)) # [1,3]
print(Solution().topKFrequent([1], 1)) # [1]