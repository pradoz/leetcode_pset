from typing import List
from heapq import heapify, heappush, heappop

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        duration = 0

        for dur, ending in courses:
            heap.append((ending, dur))
            duration += dur
        heapify(heap)

        result = 0
        
        while heap:
            print(duration, heap)
            # heappush(heap, -dur)
            end, dur = heappop(heap)

            if duration - dur < end:
                duration -= dur
                result += 1

        return result



# O(nlogn) time / O(n) space
class Solution0:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        duration = 0

        for dur, ending in sorted(courses, key=lambda x: x[1]):
            heappush(heap, -dur)

            duration += dur
            if duration > ending:
                duration += heappop(heap)

        return len(heap)








courses = [
            [[100,200],[200,1300],[1000,1250],[2000,3200]],
            [[1,2]],
            [[3,2],[4,3]],
          ]

test_results = [3,1,0]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.scheduleCourse(courses[i])
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
