'''
There is a robot starting at position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves,
judge if this robot ends up at (0, 0)after it completes its moves.

The move sequence is represented by a string,
and the character moves[i] represents its ith move.
Valid moves are R (right), L (left), U (up), and D (down).

If the robot returns to the origin after it finishes all of its moves,
return true. Otherwise, return false.
'''
# best runtime complexity solutions
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Base cases
        if moves == '':
            return True
        if moves.count('L') == moves.count('R') \
                            and moves.count('U') == moves.count('D'):
            return True
        return False

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves == '':
            return True
        return moves.count('L') == moves.count('R') \
                            and moves.count('U') == moves.count('D')

# best space complexity solutions
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves == '':
            return True
        updown, leftright = 0, 0

        for move in moves:
            if move == 'U': updown += 1
            elif move == 'D': updown -= 1
            elif move == 'L': leftright += 1
            else: leftright -= 1
        return updown == 0 and leftright == 0

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves == '':
            return True
        udlr = [0, 0]

        for move in moves:
            if move == 'U': udlr[0] += 1
            elif move == 'D': udlr[0] -= 1
            elif move == 'L': udlr[1] += 1
            else: udlr[1] -= 1
        return udlr == [0, 0]






