class Solution:
    def interpret(self, command: str) -> str:
        result = []

        idx = 0
        while idx < len(command):
            ch = command[idx]
            if ch != '(':
                result.append(ch)
                idx += 1
            elif ch == '(':
                idx += 1
                if command[idx] == ')':
                    result.append('o')
                    idx += 1
                else:
                    while command[idx] != ')':
                        result.append(command[idx])
                        idx += 1
                    idx += 1

        return ''.join(result)








command = ["G()(al)", "G()()()()(al)", "(al)G(al)()()G"]

test_results = ["Goal", "Gooooal", "alGalooG"]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.interpret(command[i])
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
