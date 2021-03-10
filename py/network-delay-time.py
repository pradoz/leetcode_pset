import collections

# DFS
class SolutionDFS:
    def networkDelayTime(self, times: [[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in range(1, n+1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return
            dist[node] = elapsed
            for time, next_node in sorted(graph[node]):
                dfs(next_node, elapsed + time)

        dfs(k, 0)
        max_dist = max(dist.values())
        # print(graph)
        return max_dist if max_dist < float('inf') else -1


# Djikstra's array implementation
# Time  O(V^2 + E)
# Space O(V + E)
class SolutionDJARR:
    def networkDelayTime(self, times: [[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, n+1)}
        visited = [False] * (n+1)
        dist[k] = 0 # start node

        while True:
            curr_node = -1
            check_dist = float('inf')
            for i in range(1, n+1):
                if not visited[i] and dist[i] < check_dist:
                    check_dist = dist[i]
                    curr_node = i

            if curr_node < 0: break
            visited[curr_node] = True

            for next_dest, edge_length in graph[curr_node]:
                dist[next_dest] = min(dist[next_dest], dist[curr_node] + edge_length)

        time_taken = max(dist.values())
        # print(graph)
        return time_taken if time_taken < float('inf') else -1



# Djikstra's heap implementation
# Time  O(E log(E)) (full heap)
# Space O(V + E)
import heapq
class Solution:
    def networkDelayTime(self, times: [[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        prio_queue = [(0, k)]
        dist = {}
        while prio_queue:
            # print(prio_queue)
            d1, node = heapq.heappop(prio_queue)
            if node in dist: continue
            dist[node] = d1
            for next_dest, d2 in graph[node]:
                if next_dest not in dist:
                    heapq.heappush(prio_queue, (d1 + d2, next_dest))
        return max(dist.values()) if len(dist) == n else -1


times = [[2,1,1],[2,3,1],[3,4,1]]
n = len(times) + 1
k = 2
print(Solution().networkDelayTime(times, n, k))