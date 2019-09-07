# Time complexity: O(n*logn) - for each new element in the stream, we insert
#                              into the heap which is log(n) for rebalancing.
# Space complexity: O(n) - we need to store all the elements in the stream in
#                          the heaps.

# Solution 1, using a min and max heap

from heapq import *

class MedianFinder:
    def __init__(self):
        """ initialize your data structure here. """
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heappush(self.max_heap, -heappushpop(self.min_heap, -num))
        else:
            heappush(self.min_heap, -heappushpop(self.max_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            min_root = self.min_heap[0]
            max_root = self.max_heap[0]
            return (max_root - min_root) / 2.0
        else:
            return self.max_heap[0]


# Solution 2, minimizing space on the heaps

from heapq import *

class MedianFinder:
    def __init__(self):
        """ initialize your data structure here. """
        self.min_heap = []
        self.max_heap = []


    def addNum(self, num: int) -> None:
        # If we find a value greater than the top of max_heap, add to max_heap
        if len(self.max_heap) == 0 or num > self.max_heap[0]:
            heappush(self.max_heap, num)

            # While the min_heap is smaller than the max_heap in size/length,
            # pop a value from max_heap, and add the negative to min_heap
            while len(self.min_heap) + 1 < len(self.max_heap):
                heappush(self.min_heap, -heappop(self.max_heap))

        # If we find a value less than the top of min_heap, add to min_heap
        else:
            heappush(self.min_heap, -num)
            while len(self.min_heap) > len(self.max_heap):
                heappush(self.max_heap, -heappop(self.min_heap))
        return

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            min_root = self.min_heap[0]
            max_root = self.max_heap[0]
            return (max_root - min_root) / 2.0
        else:
            return self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()