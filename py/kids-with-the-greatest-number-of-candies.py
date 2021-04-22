from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        
        result = []
        # max_needed = max(x for x in candies)
        max_needed = max(candies)

        # max_needed= 0
        # for c in range(n):
        #     max_needed = max(max_needed, candies[c])

        for c in range(n):
            if candies[c] + extraCandies < max_needed:
                result.append(False)
            else:
                result.append(True)

        return result


candies = [[2,3,5,1,3], [4,2,1,1,2], [12,1,12], [2,8,7]]
extraCandies = [3, 1, 10, 1]

test_results = [
                [True,True,True,False,True],
                [True,False,False,False,False],
                [True,False,True],
                [False, True, True]
               ]
test_cases = len(test_results)

def run_test() -> None:
    s = Solution()
    for i in range (test_cases):
        check_test = s.kidsWithCandies(candies[i], extraCandies[i])
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
