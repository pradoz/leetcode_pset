/*
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
*/

class MinStack {
public:
    // MinStack() {
    // }

    void push(int x) {
        if (!min_stack.empty()) {
            min_stack.push(Data(x, min(x, min_stack.top().min)));
        }
        else {
            min_stack.push(Data(x, x));
        }
    }

    void pop() {
        if (!min_stack.empty()) {
            min_stack.pop();
        }
    }

    int top() {
        if (!min_stack.empty()) {
            return min_stack.top().val;
        }
        else {
            return -1;
        }
    }

    int getMin() {
        if (!min_stack.empty()) {
            return min_stack.top().min;
        }
        return INT_MAX;
    }

private:
    struct Data {
        Data(int v, int m)
          :val{v}, min{m}
        { }

        int val;
        int min;
    };

    stack<Data> min_stack;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */