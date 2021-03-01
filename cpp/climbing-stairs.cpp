/*
Dynamic programming solution.
    3 integers to allocate --> O(1) space
    in the worst case, we iterate through n-2 elements, so this is order n as well.

    Runtime: O(n)
    Space:   O(1)
*/
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 1) return 1;

        int first_step = 1;
        int second_step = 2;
        int memo_next_step = 0; // memo step

        for (int i = 3; i <= n; ++i) {
            memo_next_step = first_step + second_step;
            first_step = second_step;
            second_step = memo_next_step;
        }
        return second_step;
    }
};




/*
Dynamic programming solution.
    n+1 element array --> O(n) space
    in the worst case, we iterate through n-2 elements, so this is order n as well.

    Runtime: O(n)
    Space:   O(n)
*/
class Solution {
public:
    int climbStairs(int n) {
        int stairs[n+1];
        
        stairs[0] = 1;
        stairs[1] = 1;
        for (int i = 2; i <= n; ++i) {
            stairs[i] = stairs[i-1] + stairs[i-2];
        }
        return stairs[n];
    }
};


/*
Recurisve solution: (Time limit exceeded due to no memoization)

Guess at a recurrence relationship for analysis:
    T(n) = 2 * T(n/[(n-1)(n-2)]) + O(1)
         => T(n) = O(n^{log_[(n-1)(n-2)](2)})
*/
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 1) return 1;
        return climbStairs(n-1) + climbStairs(n-2);
        /*
        int stairs[n+1];
        
        stairs[0] = 1;
        stairs[1] = 1;
        for (int i = 2; i <= n; ++i) {
            stairs[i] = stairs[i-1] + stairs[i-2];
        }
        return stairs[n];
        */
    }
};
