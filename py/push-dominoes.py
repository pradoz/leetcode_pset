# Time Complexity is O(n) since we do 3 linear passes on the dominoes
# Space Complexity is O(n) to construct the result forces

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        totalForces = [0] * N

        force = 0

        # Define right forces to be positive
        for currDom in range(N):
            if dominoes[currDom] == 'R':
                force = N
            elif dominoes[currDom] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            totalForces[currDom] += force


        # Define left forces to be negative
        for currDom in range(N-1, -1, -1):
            if dominoes[currDom] == 'L':
                force = N
            elif dominoes[currDom] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            totalForces[currDom] -= force


        # Construct result
        result = []
        for currForce in totalForces:
            if currForce == 0:
                result.append('.')
            elif currForce > 0:
                result.append('R')
            else: # if currForce < 0:
                result.append('L')

        # return ''.join(map(str, result))
        return ''.join(result)













print(Solution().pushDominoes(".L.R...LR..L..")) # Output: "LL.RR.LLRRLL.."
print(Solution().pushDominoes("RR.L")) # Output: "RR.L"