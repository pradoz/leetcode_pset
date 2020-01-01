'''
A maximum stack is a FIFO data structure where the maximum element can always
be accessed in O(1) time.

- if we use one array to implement the min stack, then we would only be able to
    access the min. element in, at worst, O(n) time, by traversings the array.
-- just push back new values to the end whenever push() is called, and pop back
    values whenever pop() is called.

** Time/space trade-off
- consider a second list that stores all of the maximum values
-- now we use 2n space, which is a little bit more memory, but ultimately, will
    still have linear space complexity.
-- if the new value being pushed to the stack is greater than the current max,
    then push it to the stack.
-- push and pop are O(1) even though we need to push and pop twice to both
    lists for each call to push or pop.


---- maybe try by pushing each value as a tuple initially, where the second
      index relates to the maximum value being pushed to the stack
'''


class MaxStack(object):
    def __init__(self):
        self.stack = []
        self.maxes = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #       -1  x
        # [1, 2, 3, 2]

        if self.maxes and self.maxes[-1] > val:
            # temp variable, because assigning an array lookup into its own
            # array just feels wrong.
            currentMax = self.maxes[-1]
            self.maxes.append(currentMax)
        else: # case: val > self.maxes[-1]
            self.maxes.append(val)

    def pop(self) -> int:
        if self.maxes: # exit early if no elements in the max stack
            self.maxes.pop()
        return self.stack.pop()

    def max(self) -> int:
        if self.maxes:
            return self.maxes[-1]






''' TEST CASES '''
s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print('max', s.max()) # max 3
print(s.pop()) # 2
print('max', s.max()) # max 3
print(s.pop()) # 3
print('max', s.max()) # max 2
print(s.pop()) # 2
print('max', s.max()) # max 1
print(s.pop()) # 1