# Time complexity is O(n) because we have to iterate through all 3 lists with
#       conditional statements and array lookups as extra work.
# Space complexity is O(n) in the worst case where all 3 lists are the same. If
#       this happens, the result is the same length as the input array. 
class Solution:
    def intersection(self, list1, list2, list3: [int]) -> [int]:
        index1 = 0
        index2 = 0
        index3 = 0
        result = []

        while index1 < len(list1) and index2 < len(list2) and index3 < len(list3):
            if list1[index1] == list2[index2] == list3[index3]:
                result.append(list1[index1])
                index1 += 1
                index2 += 1
                index3 += 1
                continue # jump back to while loop condition

            maxNum = max(list1[index1], list2[index2], list3[index3])

            # print(index1, index2, index3)
            # print(maxNum, "\n")
            if list1[index1] < maxNum:
                index1 += 1
            if list2[index2] < maxNum:
                index2 += 1
            if list3[index3] < maxNum:
                index3 += 1
        return result

print(Solution().intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
# [4]