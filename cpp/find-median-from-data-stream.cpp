// Time complexity: O(n*logn) - for each new element in the stream, we insert
//                              into the heap which is log(n) for rebalancing.
// Space complexity: O(n) - we need to store all the elements in the stream in
//                          the heaps.

// Solution 1 using a priority_queue as a min and max heap

class MedianFinder {
public:
    void addNum(int num) {
        // Build heap
        min_heap.push(num);
        max_heap.push(-min_heap.top());
        min_heap.pop();

        // Balance heap
        if (min_heap.size() < max_heap.size()) {
            min_heap.push(-max_heap.top());
            max_heap.pop();
        }
    }

    double findMedian() {
        return min_heap.size() > max_heap.size()
               ? min_heap.top()
               : (min_heap.top() - max_heap.top()) / 2.0;
    }
private:
    priority_queue<long> min_heap, max_heap;
};


// Solution 2 using a priority_queue with 3 parameters

class MedianFinder {
public:
    void addNum(int num) {
        // Build heaps with condition:
        // Let min_heap.size() <= max_heap.size()
        if (max_heap.empty()) {
            max_heap.push(num);
        }
        else if (max_heap.size() == min_heap.size()) {
            if (num >= min_heap.top()) {
                max_heap.push(min_heap.top());
                min_heap.pop();
                min_heap.push(num);
            }
            else {
                max_heap.push(num);
            }
        }
        else {
            if (num >= max_heap.top()) {
                min_heap.push(num);
            }
            else {
                min_heap.push(max_heap.top());
                max_heap.pop();
                max_heap.push(num);
            }
        }
    }

    double findMedian() {
        return min_heap.size() != max_heap.size()
               ? max_heap.top()
               : (min_heap.top() + max_heap.top()) / 2.0;
    }
private:
    priority_queue<int, vector<int>> max_heap;
    priority_queue<int, vector<int>, greater<int>> min_heap;
};