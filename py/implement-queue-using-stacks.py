# Best runtime complexity solution
class MyQueue:
    def __init__(self):
        """ Initialize your data structure here. """
        self.arr = []
        
    def push(self, x: int) -> None:
        """ Push element x to the back of queue. """
        self.arr.append(x)

    def pop(self) -> int:
        """ Removes the element from in front of queue and returns """
        f = self.arr[0]
        del self.arr[0]
        return f
        
    def peek(self) -> int:
        """ Get the front element. """
        return self.arr[0]

    def empty(self) -> bool:
        """ Returns whether the queue is empty. """
        return len(self.arr) == 0

# Best space complexity solution
class MyQueue:
    def __init__(self):
        """ Initialize your data structure here. """
        self.arr = []
        
    def push(self, x: int) -> None:
        """ Push element x to the back of queue. """
        self.arr.append(x)

    def pop(self) -> int:
        """ Removes the element from in front of queue and returns """
        return self.arr.pop(0)
        
    def peek(self) -> int:
        """ Get the front element. """
        return self.arr[0]

    def empty(self) -> bool:
        """ Returns whether the queue is empty. """
        return True if not self.arr else False