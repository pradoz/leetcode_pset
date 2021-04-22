from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        m = len(wall)
        n = sum(wall[0])

        if n == 1:
            return m

        freq = {}
        for layer in wall:
            ending = 0
            for i in range(len(layer)-1):
                brick = layer[i]

                ending += brick
                if ending not in freq:
                    freq[ending] = 1
                else:
                    freq[ending] += 1

        result = max((v for v in freq.values()), default=0)
        return m - result

'''
solution:
    find all the edges.
    -- each edge goes from (start, end) of the block
    -- i.e. for a block of size 1:
           |  _________  |
           | |    1    | |
           |  ---------  |
           |-------------| <-- number line
           0             1
    keep track of the number of each edge we see in a map
    look for the edge that occurs in the most rows of the wall
    see if any edges with maximum freq.'s instersect?
'''




wall = [
        [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]],
        [[1],
         [1],
         [1],
         [1],
         [1]],
        [[2],
         [1,1]],
        [[2],
         [1,1],
         [2]],
       ]

test_results = [2, 5, 1, 2]
test_cases = len(test_results)

def run_test() -> None:
    s = Solution()
    for i in range (test_cases):
        check_test = s.leastBricks(wall[i])
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
