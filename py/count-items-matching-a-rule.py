from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        result = 0
        for item in items:
            if self.is_match(ruleKey, ruleValue, item):
                result += 1


        return result

    def is_match(self, key: str, val: str, item: List[str]) -> bool:
        if key == 'type':
            return val == item[0]
        if key == 'color':
            return val == item[1]
        if key == 'name':
            return val == item[2]
        return False







items = [
         [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],
         [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],
        ]
ruleKey = ["color", "type",]
ruleValue = ["silver", "phone",]

test_results = [1,2]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.countMatches(items[i], ruleKey[i], ruleValue[i])
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
