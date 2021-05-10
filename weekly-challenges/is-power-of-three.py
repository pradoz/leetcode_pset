class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0: return False # lower bound of problem statement
        
        while n % 3 == 0:
            # digit = num % 3
            n //= 3

        # result = True if n == 1 else False
        # return result
        return n == 1








n= [27, 0, 9, 45]

test_results = [True, False, True, False]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.isPowerOfThree(n[i])
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
