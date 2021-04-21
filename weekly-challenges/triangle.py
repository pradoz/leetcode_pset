from typing import List

class Solution: # top-down
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) < 2:
            return triangle[0][0]

        m = len(triangle)
        # n = len(triangle[m-1])

        # one total for each path to the bottom
        path_costs = [triangle[0][0] for _ in range(m)] 
        # path_costs = triangle[-1]

        for i in range(1, m):
            cols = triangle[i]
            for j in range(i, -1, -1):
                if j == 0:
                    path_costs[0] += cols[j]
                elif j == i:
                    path_costs[j] = cols[j] + path_costs[j-1]
                else:
                    path_costs[j] = cols[j] + min(path_costs[j], path_costs[j-1])

        return min(cost for cost in path_costs)



class Solution0:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) < 2:
            return triangle[0][0]

        m = len(triangle)
        n = len(triangle[m-1])

        # one total for each path to the bottom
        path_costs = [triangle[m-1][i] for i in range(n)] 
        # path_costs = triangle[-1]

        # path_costs[i] = min(path_costs[i], path_costs[i+1]) + current_entry
        for i in range(m-2, -1, -1): # bottom-up
            cols = triangle[i]
            for j in range(len(cols)):
                path_costs[j] = cols[j] + min(path_costs[j], path_costs[j+1])

        return path_costs[0]








triangle = [[[2],[3,4],[6,5,7],[4,1,8,3]], [[-10]], [[1],[2,3]]]

test_results = [11, -10, 3]
test_cases = len(test_results)

def run_test() -> None:
    s = Solution()
    for i in range (test_cases):
        check_test = s.minimumTotal(triangle[i])
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
