class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = [0] * (len(num1) + len(num2))
        lastDecimalPlace = len(product) - 1
        
        for n1 in reversed(num1):
            currDecimalPlace = lastDecimalPlace
            for n2 in reversed(num2):
                # product[currDecimalPlace] += int(n1) * int(n2)
                product[currDecimalPlace] += (ord(n1) - ord('0')) * (ord(n2) - ord('0'))

                # get the next digit
                product[currDecimalPlace - 1] += product[currDecimalPlace] // 10
                product[currDecimalPlace] %= 10

                currDecimalPlace -= 1
            lastDecimalPlace -= 1
            
        pt = 0
        # skip over any leading zeroes
        while pt < len(product) - 1 and product[pt] == 0:
            pt += 1

        return ''.join(map(str, product[pt:]))










num1 = '2'
num2 = '3'
print(Solution().multiply(num1, num2)) # '6'

num1 = '123'
num2 = '456'
print(Solution().multiply(num1, num2)) # '56088'

num1 = '123456789'
num2 = '987654321'
print(Solution().multiply(num1, num2)) # '121932631112635269'