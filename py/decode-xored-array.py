from typing import List
'''
first = 1
           i
[1,   2,   3]

decoded
[0,   0,   0,   1]
[1,   0,   2,   1]
'''
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        decoded = [first] + [0] * n
        for i in range(n):
            # print(decoded[i], first, first ^ decoded[i])
            decoded[i+1] = encoded[i] ^ decoded[i]

        return decoded








encoded = [[1,2,3], [6,2,7,3], [0,0,5,3]]
first = [1,4,7]

test_results = [[1,0,2,1],[4,2,0,7,4],[7,7,7,2,1]]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.decode(encoded[i], first[i])
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
