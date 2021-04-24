from typing import List
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(rank: int, node: int, prev: int) -> None:
            # print(visited)
            # print(f'calling dfs(rank={rank}, node={node}, prev={prev})')
            # print(f'setting visited[node] = visited[{node}] = rank = {rank}')
            visited[node] = rank
            for neighbor in servers[node]:
                if neighbor == prev: # avoid traversing backwards
                    continue
                if not visited[neighbor]:
                    dfs(rank + 1, neighbor, prev=node)
                    # print(f'calling dfs(rank+1={rank+1}, neighbor={neighbor}, prev={node})')

                visited[node] = min(visited[node], visited[neighbor])
                if visited[neighbor] >= rank + 1:
                    result.append([node, neighbor])

        servers = defaultdict(list)
        # create an undirected graph
        for u, v in connections:
            servers[u].append(v)
            servers[v].append(u)

        # print(servers)
        result = []
        visited = [0 for _ in range(n)]

        dfs(rank=1, node=0, prev=-1)
        return result








connections = [
               [[0,1],[1,2],[2,0],[1,3]],
              ]
n = [4]

test_results = [
                [[1,3]],
               ]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.criticalConnections(n[i], connections[i])
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
