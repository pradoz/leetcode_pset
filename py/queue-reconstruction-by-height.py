# time complexity is nlogn for the sort, n^2 for the sorting by k => O(n^2)
# space complexity is O(n) to store all the people's [h,k] values
class Solution:
    def reconstructQueue(self, people: [[int]]) -> [[int]]:
        # people.sort(reverse=True)
        # sort heights, put tall people first
        people.sort(key=lambda person: (-person[0], person[1]))

        result = []

        # order by k
        for person in people:
            k = person[1]
            result.insert(k, person) # can be o(n) in worst case

        return result



print(Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
# [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]