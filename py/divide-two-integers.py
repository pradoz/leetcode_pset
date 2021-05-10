class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        # think then code
        '''
        18 / 3
        ------
        1 | 18-3=15
        ...
        6 | 3-3=0
        ~~~~~~~~~
        10 / 3
        ------
        1 | 10-3=7
        2 | 7-3=4
        3 | 4-3=1
        4 | 1-3=-2 --> dont increcement result
        '''
        is_negative = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            is_negative = True

        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1

        result = result if is_negative != True else -result
        return min(max(-2147483648, result), 2147483647)








dividend = [10,7,0,1]
divisor = [3,-3,1,1]

test_results = [3,-2,0,1]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.divide(dividend[i], divisor[i])
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
