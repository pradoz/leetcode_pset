from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        result = []

        # think then code
        path_counter = defaultdict(list)
        for p in paths:
            split_path = p.split(' ')
            file_dir = split_path[0]
            for file_name in split_path[1:]:
                file_info = file_name.split('(')
                file_path = split_path[0] + '/' + file_info[0]
                file_contents = file_info[1][0:len(file_info[1])-1]
                path_counter[file_contents].append(file_path)
            #     print(f'ZZZZ path_counter: {path_counter}')
            #     print(f'XXXX info: {file_info}')
            #     print(f'XXXX path: {file_path}')
            #     print(f'XXXX filename: {file_name}')
            #     print(f'~~~~ content: {file_contents}')
            # print('-' * 20)

        for key, val in path_counter.items():
            if len(path_counter[key]) > 1:
                result.append(val)

        return result








paths = [
        ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"],
        ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"],
       ]

test_results = [
        [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]],
        [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]],
        ]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.findDuplicate(paths[i])
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
