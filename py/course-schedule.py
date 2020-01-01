# detecting cycles in a digraph to determine if a topological sort can be
# obtained from the input of prerequisites.

'''
For every node in the graph, we need to:
  1. start at a node, mark it as visited
  2. mark every node that each node can reach as visited successively
  3. if we hit a node that was already visited, then we found a cycle
  4. if we found a cycle, then return false. return true otherwise.
'''

# Time Complexity O(n^2) in the case where the graph is strongly connected we
#     have to visit every node in the graph for each node we start at.
# Space Complexity O(n^2) since we have to store all n nodes and at most n nodes
#     for every other node in the graph.



# defaultdict will assign an empty list by default now
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a map of keys and lists of paths
        graph = defaultdict(list)

        # 
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])

        # if we add a duplicate path in visited, we found a cycle
        visited = set()

        # returns true if there is a cycle, and false otherwise.
        def detectCycle_DFS(vertex):
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor in visited or detectCycle_DFS(neighbor):
                    return True

            # reset the visited set for next dfs call
            visited.remove(vertex)
            return False

        # iterate through every course and return false if we find a cycle
        for i in range(numCourses):
            if detectCycle_DFS(i) == True:
                return False
        return True

