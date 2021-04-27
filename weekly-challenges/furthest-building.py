from typing import List
from heapq import heappush, heappop

# use ladders on largest jumps
# use bricks on smaller jumps
# --> keep a minimum heap.. once its size is bigger than the number of ladders
#     and we are out of bricks, that is the number of moves.
# time O(n*logk) for n buildings with k ladders
# space O(k) to store heights equal to the number of ladders
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)

        jumps = []
        for i in range(0, n-1):
            jump = heights[i+1] - heights[i] 
            if jump <= 0:
                continue

            heappush(jumps, jump)
            if len(jumps) > ladders:
                bricks -= heappop(jumps)

            if bricks < 0:
                return i

        return n - 1








heights = [[4,2,7,6,9,14,12],
        [4,12,2,7,3,18,20,3,19],
        [14,3,19,3],
        [4,2,7,6,9,14,12],
        [1,5,1,2,3,4,10000],
    ]
bricks = [5,10,17,5,4]
ladders = [1,2,0,1,1]

test_results = [4,7,3,4,5]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.furthestBuilding(heights[i], bricks[i], ladders[i])
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
